from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

"""Importing the sys module to manipulate import path"""
import sys

sys.path.append("src")

from model.Payroll_Logic import *

class WelcomePopup(Popup):
    def __init__(self, **kwargs):
        super(WelcomePopup, self).__init__(**kwargs)
        """Title of the Popup"""
        self.title = 'Payroll payment'
        self.background_color = [8, 8, 8, 8]  
        main_box = BoxLayout(orientation='vertical')
        
        """BoxLayout for the image"""
        image_box = BoxLayout()
        image = Image(source='53419.jpg')
        image_box.add_widget(image)
        
        """Creating a vertical BoxLayout for the content and a label widget with welcome message"""
        content_box = BoxLayout(orientation='vertical')
        label = Label(text='Welcome to the payroll payment App', font_size='35sp', halign='center', color=[0, 0, 0, 1])  
        with label.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=label.size, pos=label.pos)
        label.bind(size=self._update_rect, pos=self._update_rect)
        
        button_box = BoxLayout(orientation='horizontal')
        button = Button(text='Calculate your payroll', background_color=[0.5, 0.5, 1, 1], size_hint=(.7, .7))
        """Binding button press to dismiss the Popup"""
        button.bind(on_press=self.dismiss)
        button_box.add_widget(Widget())  
        button_box.add_widget(button)
        button_box.add_widget(Widget())  
        
        content_box.add_widget(label)
        content_box.add_widget(button_box)
        
        """Adding the BoxLayouts to the main BoxLayout"""
        main_box.add_widget(image_box)
        main_box.add_widget(content_box)
        
        self.content = main_box

        

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

"""Creating the input data widgets using a GridLayout"""
class GUIPayrollApp(App):
    def build(self):
        Window.clearcolor = 'white'
        layout = GridLayout(cols=2, padding=80)

    
        layout.add_widget( Label(text="Basic salary", color= 'black', halign='left'))
        self.basic_salary = TextInput(font_size=20)
        layout.add_widget(self.basic_salary)

        #layout.add_widget( Label(text="Transport subsidy", color= 'black') )
        #self.transport = TextInput(font_size=20)
        #layout.add_widget(self.transport)

        layout.add_widget( Label(text="Worked days", color= 'black') )
        self.worked_days = TextInput(font_size=20)
        layout.add_widget(self.worked_days)

        layout.add_widget( Label(text="Holiday worked days", color= 'black') )
        self.holidayworked_days = TextInput(font_size=20)
        layout.add_widget(self.holidayworked_days)

        layout.add_widget( Label(text="Extra light worked hours", color= 'black') )
        self.extralightworked_hours = TextInput(font_size=20)
        layout.add_widget(self.extralightworked_hours)

        layout.add_widget( Label(text="Extra night worked hours", color= 'black') )
        self.extranightworked_hours = TextInput(font_size=20)
        layout.add_widget(self.extranightworked_hours)

        layout.add_widget( Label(text="Holiday extra daylight worked hours", color= 'black') )
        self.holidaylighthours = TextInput(font_size=20)
        layout.add_widget(self.holidaylighthours)

        layout.add_widget( Label(text="Holiday extra night worked hours", color= 'black') )
        self.holidaynighthours = TextInput(font_size=20)
        layout.add_widget(self.holidaynighthours)

        layout.add_widget( Label(text="Health insurance percentage", color= 'black') )
        self.health = TextInput(font_size=20)
        layout.add_widget(self.health)
        
        layout.add_widget( Label(text="Pension contribution percentage", color= 'black') )
        self.pension = TextInput(font_size=20)
        layout.add_widget(self.pension)
        
        layout.add_widget( Label(text="Pension solidarity fund contribution percentage", color= 'black') )
        self.pension_solidarity = TextInput(font_size=20)
        layout.add_widget(self.pension_solidarity)
        
        layout.add_widget( Label(text="Days of disability", color= 'black') )
        self.disability = TextInput(font_size=20)
        layout.add_widget(self.disability)
        
        layout.add_widget( Label(text="Leave days", color= 'black') )
        self.leave_days = TextInput(font_size=20)
        layout.add_widget(self.leave_days)

        self.result = Label()
        layout.add_widget(self.result)

        layout.add_widget(Widget())

        calculate_button = Button(text="Calculate payroll", background_color=[0.5, 0.5, 1, 1])
        calculate_button.bind(on_press=self.calculate_payroll)
        layout.add_widget(calculate_button)

       
        """Creating the button to calculate everything"""
        self.result_label = Label(text="", color='black')
        layout.add_widget(self.result_label)
        

        
        
        return layout
    

    """Creating exceptions to catch errors"""
    def calculate_payroll(self, sender):
        try:
            salary = float(self.basic_salary.text)
            if salary < 30000:
                self.result_label.text = "Salary can't be less than 30000"
                return
        except ValueError:
            self.result_label.text = "invalid value for salary , please correct it."
            return

        try:
            workeddays = int(self.worked_days.text)
            if workeddays > 30:
                self.result_label.text = "30 days cannot be exceeded for the payroll process."
                return
        except ValueError:
            self.result_label.text = "invalid value for worked days , please correct it."
            return

        try:
            holidaytimeworked = int(self.holidayworked_days.text)
            if holidaytimeworked > 3:
                self.result_label.text = "The maximum holiday days in a month is 3 holidays"
                return
        except ValueError:
            self.result_label.text = "invalid value for Holiday worked days , please correct it."
            return

        try:
            extralighthoursworked = int(self.extralightworked_hours.text)
            if extralighthoursworked > 12 :
                self.result_label.text = "The maximum of extra light hours to work is 12"
                return
        except ValueError:
            self.result_label.text = "invalid value for Extra light worked hours , please correct it."
            return

        try:
            extranighthoursworked = int(self.extranightworked_hours.text)
            if extranighthoursworked > 12 :
                self.result_label.text = "The maximum of extra night hours to work is 12"
                return
        except ValueError:
            self.result_label.text = "invalid value for Extra night worked hours , please correct it."
            return

        try:
            extraholidaylighthours = int(self.holidaylighthours.text)
            if extraholidaylighthours > 12 :
                self.result_label.text = "The maximum of holiday extra light hours to work is 12"
                return
        except ValueError:
            self.result_label.text = "invalid value for Holiday extra daylight worked hours , please correct it."
            return

        try:
            extraholidaynighthours = int(self.holidaynighthours.text)
            if extraholidaynighthours > 12 :
                self.result_label.text = "The maximum of holiday extra night hours to work is 12"
                return
        except ValueError:
            self.result_label.text = "invalid value for Holiday extra night worked hours , please correct it."
            return

        try:
            healthinsurance = int(self.health.text)
            if healthinsurance > 4 :
                self.result_label.text = "The health insurance may not exceed 4%"
                return
        except ValueError:
            self.result_label.text = "invalid value for Health insurance percentage , please correct it."
            return

        try:
            pensioncontribution = int(self.pension.text)
            if pensioncontribution > 4 :
                self.result_label.text = "The pension contribution may not exceed 4%"
                return
        except ValueError:
            self.result_label.text = "invalid value for Pension contribution percentage , please correct it."
            return

        try:
            solidarity = int(self.pension_solidarity.text)
            if solidarity > 2.8 :
                self.result_label.text = "The maximum of the solidarity fund may not exceed 2.8%"
                return
        except ValueError:
            self.result_label.text = "invalid value for Pension solidarity fund contribution percentage , please correct it."
            return

        try:
            disabilitydays = int(self.disability.text)
            if pensioncontribution > 30 :
                self.result_label.text = "The disability days may not exceed 30 days"
                return
        except ValueError:
            self.result_label.text = "invalid value for Days of disability , please correct it."
            return

        try:
            leavedays = int(self.leave_days.text)
            if leavedays > 30 :
                self.result_label.text = "The leave days may not exceed 30 days"
                return
        except ValueError:
            self.result_label.text = "invalid value for leave days , please correct it."
            return

        
        accruals = Accruals(salary, workeddays, holidaytimeworked, extralighthoursworked, extranighthoursworked,
                            extraholidaylighthours, extraholidaynighthours, disabilitydays, leavedays)


        deductions = Deductions(accruals, healthinsurance, pensioncontribution, solidarity)

        """If all the values ​​are valid, then proceed with the calculations"""
        Withhold = deductions.CalculateWithholdingTax()
        salary_calculator = SalaryCalculator(accruals, deductions)
        

        self.result.text = str(salary_calculator)

    
        """Applying bold and italic to the text of the results"""
        
        output = f"""
        The salary is: [i][b]{salary}[/b][/i]
        The value to be paid for holidays is:  [i][b]{holidaytimeworked}[/b][/i]
        The value to be paid for daylight extra hours is:  [i][b]{extralighthoursworked}[/b][/i]
        The value to be paid for night extra hours is:  [i][b]{extranighthoursworked}[/b][/i]
        The value to be paid for holiday extra daylight hours is:  [i][b]{extraholidaylighthours}[/b][/i]
        The value to be paid for holiday night extra hours is:  [i][b]{extraholidaynighthours}[/b][/i]
        The value of the health contribution is:  [i][b]{healthinsurance}[/b][/i]
        The value of the pension contribution is:  [i][b]{pensioncontribution}[/b][/i]
        The value of the solidarity fund contribution is:  [i][b]{solidarity}[/b][/i]
        The value of the disability days is:  [i][b]{disabilitydays}[/b][/i]
        The value of leave days is:  [i][b]{leavedays}[/b][/i]
        The value of the withholding tax for [i][b]${salary}:[/b][/i] is [i][b]${Withhold}[/b][/i]
        The total value to be paid is:  [i][b]{salary_calculator}[/b][/i]
        """
        popup = ResultPopup(output)
        popup.open()
        

    def on_start(self):
        popup = WelcomePopup()
        popup.open()



"""Creating a popup window to display the output variables and results"""
class ResultPopup(Popup):
    def __init__(self, result, **kwargs):
        super(ResultPopup, self).__init__(**kwargs)
        self.title = 'Payroll Results'  
        self.background_color = [1, 1, 1, 1]  

        main_box = FloatLayout()
        with main_box.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = Rectangle(size=main_box.size, pos=main_box.pos)
        main_box.bind(size=self._update_rect, pos=self._update_rect)

        """Boxlayout for the content"""
        content_box = BoxLayout(orientation='vertical', size_hint=(1, 0.8), pos_hint={'x': 0, 'y': 0.1}) 
        label = Label(text=result, font_size='20sp', halign='left', color=[0, 0, 0, 1], bold=False, markup= True) 
        with label.canvas.before:
            Color(1, 1, 1, 1) 
            self.rect_label = Rectangle(size=label.size, pos=label.pos)
        label.bind(size=self._update_rect_label, pos=self._update_rect_label)

        content_box.add_widget(label)

        """BoxLayout for the buttons"""
        button_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), pos_hint={'x': 0, 'y': 0})

        """Return button"""
        back_button = Button(text='Return', size_hint=(0.5, 1), background_color=(0, 0, 1, 1))
        back_button.bind(on_press=self.dismiss)
        button_box.add_widget(back_button)

        """Close App button"""
        close_button = Button(text='Close App', size_hint=(0.5, 1), background_color=(0, 0, 1, 1))
        close_button.bind(on_press=self.close_app)  
        button_box.add_widget(close_button)

        content_box.add_widget(button_box)

        main_box.add_widget(content_box)

        image = Image(source='1234.jpg', size_hint=(None, None), size=(150, 150), pos_hint={'right': 1, 'top': 1})
        main_box.add_widget(image)

        self.content = main_box

    """Updating the position and size of the 'rect' widget to match the position of the 'instance' widget"""
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    """Updating the position, size and text size of the 'rect_label' widget"""
    def _update_rect_label(self, instance, value):
        self.rect_label.pos = instance.pos
        self.rect_label.size = instance.size
        instance.text_size = (instance.width, None)

    def close_app(self, instance):
        App.get_running_app().stop()


def main():
    GUIPayrollApp().run()
      
if __name__ == "__main__":
    main()
