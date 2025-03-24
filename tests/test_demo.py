from pages.widgets import WidgetsPagesTest
from pages.alert import AlertPagesTest




def test_date_picker(driver,wait):
    
    widgetsPagesTest = WidgetsPagesTest(driver,wait)
    widgetsPagesTest.click_widgets()
    widgetsPagesTest.click_datepicker()
    widgetsPagesTest.click_date()
    widgetsPagesTest.prosgress_bar()





def test_Menu_Alert(driver,wait):
    
    alertPagesTest = AlertPagesTest(driver,wait)
    alertPagesTest.go_alert()

    


