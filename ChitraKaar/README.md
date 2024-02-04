# ChitraKaar
**Usage**
1. Open the provided Python script ChitraKaar.py in your preferred code editor.
2. Replace the placeholder values in the script as needed (e.g., model name, GPU device, etc.).
3. Run the script to launch the Gradio interface.
   
bash
Copy python script.py code

Access the Gradio interface by navigating to the provided link (e.g., http://127.0.0.1:7860).
Interface Instructions
Input: Enter a text prompt in the input box.
Parameters (optional): Adjust the height, width, steps, and guidance parameters as needed.
Click "Submit" to generate an image based on the input prompt.
Additional Notes
The provided negative_prompt variable can be customized for generating specific types of images.
The interface is set to not update live (live=False). You can manually trigger the interface to submit using the provided line in the script.
Dependencies
gradio==2.1.0
torch==1.10.0
diffusers==0.1.0
transformers==4.12.2
accelerate==0.6.0
