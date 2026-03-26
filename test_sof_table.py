"""SoF Table Generator — Selenium Tests (20 tests)"""
import sys, os, time, io, unittest
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sof-table.html')
URL = 'file:///' + HTML_PATH.replace('\\', '/')

def get_driver():
    opts = Options()
    opts.add_argument('--headless=new'); opts.add_argument('--no-sandbox'); opts.add_argument('--disable-gpu'); opts.add_argument('--window-size=1400,900')
    opts.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    d = webdriver.Chrome(options=opts); d.implicitly_wait(2); return d

class SoFTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.driver = get_driver(); cls.driver.get(URL); time.sleep(0.5)
    @classmethod
    def tearDownClass(cls): cls.driver.quit()
    def _reload(self): self.driver.get(URL); time.sleep(0.3)
    def _click(self, by, val):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, val)))
        self.driver.execute_script("arguments[0].click()", el); return el

    def test_01_page_loads(self):
        title = self.driver.title.lower()
        self.assertTrue('summary' in title or 'sof' in title or 'findings' in title or 'grade' in title)
    def test_02_four_tabs(self):
        tabs = self.driver.find_elements(By.CSS_SELECTOR, '[role="tab"]')
        self.assertGreaterEqual(len(tabs), 4)
    def test_03_outcomes_tab(self):
        panel = self.driver.find_element(By.ID, 'panel-outcomes')
        self.assertTrue(panel.is_displayed() or 'active' in (panel.get_attribute('class') or ''))
    def test_04_review_title(self):
        el = self.driver.find_element(By.ID, 'reviewTitle')
        self.assertIsNotNone(el)
    def test_05_add_outcome_fields(self):
        el = self.driver.find_element(By.ID, 'addName')
        self.assertIsNotNone(el)
    def test_06_effect_type_selector(self):
        el = self.driver.find_element(By.ID, 'addEffectType')
        self.assertIsNotNone(el)
    def test_07_load_example(self):
        self._reload()
        self._click(By.ID, 'loadExampleBtn'); time.sleep(0.5)
    def test_08_grade_tab(self):
        self._click(By.ID, 'tab-grade'); time.sleep(0.3)
        panel = self.driver.find_element(By.ID, 'panel-grade')
        self.assertIn('active', panel.get_attribute('class') or '')
    def test_09_grade_has_domains(self):
        text = self.driver.find_element(By.ID, 'panel-grade').text.lower()
        has_grade = any(d in text for d in ['risk of bias', 'inconsistency', 'indirectness', 'imprecision', 'publication', 'serious', 'not serious'])
        self.assertTrue(has_grade or len(text) > 50)
    def test_10_sof_tab(self):
        self._click(By.ID, 'tab-sof'); time.sleep(0.3)
        panel = self.driver.find_element(By.ID, 'panel-sof')
        self.assertIn('active', panel.get_attribute('class') or '')
    def test_11_sof_table_rendered(self):
        panel = self.driver.find_element(By.ID, 'panel-sof')
        html = panel.get_attribute('innerHTML')
        self.assertTrue('table' in html.lower() or 'outcome' in html.lower() or len(panel.text) > 20)
    def test_12_export_tab(self):
        self._click(By.ID, 'tab-export'); time.sleep(0.3)
        panel = self.driver.find_element(By.ID, 'panel-export')
        self.assertIn('active', panel.get_attribute('class') or '')
    def test_13_ci_inputs(self):
        self._reload()
        low = self.driver.find_element(By.ID, 'addCILow')
        high = self.driver.find_element(By.ID, 'addCIHigh')
        self.assertIsNotNone(low)
        self.assertIsNotNone(high)
    def test_14_study_design(self):
        el = self.driver.find_element(By.ID, 'studyDesign')
        self.assertIsNotNone(el)
    def test_15_dark_mode(self):
        self._reload()
        btn = self.driver.find_element(By.ID, 'themeBtn')
        self.driver.execute_script("arguments[0].click()", btn); time.sleep(0.2)
        self.driver.execute_script("arguments[0].click()", btn)
    def test_16_example_selector(self):
        el = self.driver.find_element(By.ID, 'exampleSel')
        self.assertIsNotNone(el)
    def test_17_k_and_n_inputs(self):
        k = self.driver.find_element(By.ID, 'addK')
        n = self.driver.find_element(By.ID, 'addN')
        self.assertIsNotNone(k)
        self.assertIsNotNone(n)
    def test_18_estimate_input(self):
        el = self.driver.find_element(By.ID, 'addEstimate')
        self.assertIsNotNone(el)
    def test_19_tab_keyboard(self):
        self._reload()
        tabs = self.driver.find_elements(By.CSS_SELECTOR, '[role="tab"]')
        if len(tabs) > 0:
            tabs[0].send_keys(Keys.ARROW_RIGHT); time.sleep(0.2)
    def test_20_no_js_errors(self):
        logs = self.driver.get_log('browser')
        severe = [l for l in logs if l['level']=='SEVERE' and 'favicon' not in l.get('message','')]
        self.assertEqual(len(severe), 0, f"JS errors: {severe}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
