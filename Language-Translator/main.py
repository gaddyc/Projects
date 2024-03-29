import remi.gui as gui
from remi import start, App
import csv

class MyApp(App):
  def __init__(self, *args):
    self.translations = {}
    super(MyApp, self).__init__(*args)
    
  def on_button_pressed(self, widget):

    word = self.textinput.get_value()
    word = word.lower()

    if word in self.translations:
      self.spanish.set_text("SPANISH: " + self.translations[word][0])
      #ADD CODE: to display the French word
      self.french.set_text("FRENCH: " + self.translations[word][1])
      #self.error.set_text()
    else:
      self.error.set_text("Oops! Translation is not known.")

    return
   
  def main(self):
    # ADD CODE: open CSV code, DictReader, and for loop
    with open("translations.csv","r") as words:
      reader =csv.DictReader(words, delimiter=",")
      for line in reader:
        english = line["English"]
        line["English"].lower()
        spanish = line["Spanish"]
        line["Spanish"].lower()
        french = line["French"]
        line["French"].lower()

        self.translations[english] = [spanish,french]
    
    print('Type "done" at any time to exit.\n')



    # These create the various elements seen on the GUI
    container = gui.VBox(width=500, height=300, style={"box-shadow":"none"})
    self.label = gui.Label("Type an English word to translate!", width=300, height=10, style={"font-size":"16px", "font-weight":"bold", "text-align":"center"})
    self.spanish = gui.Label("SPANISH: ", width=300, height=5, style={"font-size":"14px"})
    self.french = gui.Label("FRENCH: ", width=300, height=5, style={"font-size":"14px"})
    self.textinput = gui.TextInput(width=300, height=26, style={"padding-top":"10px", "padding-left":"10px"})
    self.error = gui.Label("", width=300, height=5, style={"font-style":"italic"})
    self.button = gui.Button("TRANSLATE", width=300, height=40, margin="10px", style={"background-color":"#F16059", "font-weight":"bold", "font-size":"16px", "box-shadow":"none"})




    # Adds the elements to the GUI
    container.append(self.label)
    container.append(self.textinput)
    container.append(self.spanish)
    container.append(self.french)
    container.append(self.error)
    container.append(self.button)

    # When you click on button, call the function on_button_pressed
    self.button.onclick.connect(self.on_button_pressed)
  
    return container

start(MyApp, debug=False, address='0.0.0.0', port=0,multiple_instance=True)