import tkinter as tk
from googletrans import Translator
from indic_transliteration import sanscript


class TranslatorApp:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Translator & Transliterator")
        self.window.geometry("600x300")

        
        self.tabControl = tk.ttk.Notebook(self.window)
        self.translateTab = tk.Frame(self.tabControl)
        self.transliterateTab = tk.Frame(self.tabControl)
        self.tabControl.add(self.translateTab, text="Translate")
        self.tabControl.add(self.transliterateTab, text="Transliterate")
        self.tabControl.pack(expand=True, fill="both")

        
        self.input_frame = tk.Frame(self.translateTab)
        self.input_text = tk.Text(self.input_frame, height=10)
        self.input_text.pack(side="top", fill="both", expand=True)
        self.translate_button = tk.Button(
            self.input_frame, text="Translate", command=self.translate
        )
        self.translate_button.pack(side="bottom")
        self.choose_file_button = tk.Button(
            self.input_frame, text="Choose File", command=self.choose_file
        )
        self.choose_file_button.pack(side="bottom")
        self.choose_lang_button = tk.Button(
            self.input_frame, text="Choose Language", command=self.choose_language
        )
        self.choose_lang_button.pack(side="bottom")
        self.input_frame.pack(side="top", fill="both", expand=True)

        
        self.output_frame = tk.Frame(self.translateTab)
        self.output_text = tk.Text(self.output_frame, height=10)
        self.output_text.pack(side="top", fill="both", expand=True)
        self.copy_button = tk.Button(self.output_frame, text="Copy", command=self.copy)
        self.copy_button.pack(side="bottom")
        self.save_button = tk.Button(self.output_frame, text="Save As", command=self.save)
        self.save_button.pack(side="bottom")
        self.output_frame.pack(side="bottom", fill="both", expand=True)

        
        self.transliterate_input_frame = tk.Frame(self.transliterateTab)
        self.transliterate_input_text = tk.Text(
            self.transliterate_input_frame, height=10
        )
        self.transliterate_input_text.pack(side="top", fill="both", expand=True)
        self.transliterate_button = tk.Button(
            self.transliterate_input_frame, text="Transliterate", command=self.transliterate
        )
        self.transliterate_button.pack(side="bottom")
        self.transliterate_input_frame.pack(side="top", fill="both", expand=True)


        self.transliterate_output_frame = tk.Frame(self.transliterateTab)
        self.transliterate_output_text = tk.Text(
            self.transliterate_output_frame, height=10
        )
        self.transliterate_output_text.pack(side="top", fill="both", expand=True)
        self.transliterate_output_frame.pack(side="bottom", fill="both", expand=True)

        self.translator = Translator()
        self.transliterator = sanscript

        self.languages = ["English", "Hindi", "Urdu"]

        self.chosen_language = "en"
        
        self.window.mainloop()

    def translate(self):
        input_text = self.input_text.get(1.0, tk.END)
    
        translated_text = self.translator.translate(input_text, dest=self.chosen_language)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, translated_text.text)
 
    def translate(self):
      input_text = self.input_text.get(1.0, tk.END)
      translated_text = self.translator.translate(input_text, dest=self.chosen_language)
      self.output_text.delete(1.0, tk.END)
      self.output_text.insert(tk.END, translated_text.text)
  
    def transliterate(self):
        input_text = self.transliterate_input_text.get(1.0, tk.END)
        transliterated_text = self.transliterator.transliterate(input_text, 'urdu')
        self.transliterate_output_text.delete(1.0, tk.END)
        self.transliterate_output_text.insert(tk.END, transliterated_text)
        
    def choose_file(self):
      filename = tk.filedialog.askopenfilename(title="Select File")
      if filename:
          with open(filename, 'r') as file:
            file_contents = file.read()
            self.input_text.delete(1.0, tk.END)
            self.input_text.insert(tk.END, file_contents)


    def choose_language(self):
        language_options = self.languages
        selected_language = tk.StringVar(self.window)
        selected_language.set(self.chosen_language)
        language_dropdown = tk.OptionMenu(self.window, selected_language, *language_options)
        language_dropdown.pack(side="top")

    
    def update_language(event):
        self.chosen_language = selected_language.get()
        language_dropdown.bind("<Button-1>", update_language)


    def copy(self):
        output_text = self.output_text.get(1.0, tk.END)
        tk.clipboard.copy(output_text)
    
    def save(self):
        filename = tk.filedialog.asksaveasfilename(title="Save As")
        if filename:
            output_text = self.output_text.get(1.0, tk.END)
            with open(filename, 'w') as file:
                file.write(output_text)
            



