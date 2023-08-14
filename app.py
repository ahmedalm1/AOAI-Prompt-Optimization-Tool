import os
import openai
import tkinter as tk
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_API_ENDPOINT")

class PromptOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prompt Optimization Tool")

        self.prompt_label = tk.Label(root, text="Enter your prompt:")
        self.prompt_label.pack(pady=10)

        self.prompt_entry = tk.Entry(root, width=50)
        self.prompt_entry.pack(pady=5)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.submit_button = tk.Button(self.button_frame, text="Submit", command=self.optimize_prompt)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_input)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.response_label = tk.Label(root, text="Response:")
        self.response_label.pack(pady=10)

        self.response_text = tk.Text(root, height=10, width=50, wrap="word")
        self.response_text.pack(pady=5)

    def optimize_prompt(self):
        user_prompt = self.prompt_entry.get()

        optimized_prompt = self.optimize_prompt_with_openai(user_prompt)

        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, optimized_prompt)

    def optimize_prompt_with_openai(self, prompt):
        response = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_OPENAI_DEPLOYED_MODEL"),
            max_tokens=200,
            temperature=0.9,
            top_p=0.8,
            messages=[
                {"role": "system", "content": "Assess the provided prompt on a scale from one to ten, where one is worst, and ten is best, considering clarity, optimization, prompt engineering, effectiveness in conveying the point, and structural quality. Afterwards, rephrase it for improvement. Respond to example prompts using: \n\nGrade: \n\nReason for Grade: \n\nOptimized Prompt:"},
                {"role": "user", "content": prompt}
            ]
        )
        
        optimized_prompt = response['choices'][0]['message']['content']
        return optimized_prompt
    
    def clear_input(self):
        self.prompt_entry.delete(0, tk.END)
        self.response_text.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = PromptOptimizerApp(root)
    root.mainloop()
