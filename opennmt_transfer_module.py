# transfer_module/opennmt_transfer_module.py

from transformers import MarianMTModel, MarianTokenizer
from .transfer_module_interface import TransferModuleInterface

class OpenNMTTransferModule(TransferModuleInterface):
    def __init__(self, model_name):
        # Initialize the MarianMTModel and MarianTokenizer
        self.translation_model = MarianMTModel.from_pretrained(model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)

    def transfer(self, analysis_result):
        # Extract relevant linguistic information from analysis_result
        source_language = analysis_result.get("source_language", "en")  # Default to English if not specified
        target_language = analysis_result.get("target_language", "fr")  # Default to French if not specified
        text_to_translate = analysis_result.get("text_to_translate", "")

        # Tokenize and translate the input text
        input_ids = self.tokenizer.encode(text_to_translate, return_tensors="pt", max_length=512)
        translation_ids = self.translation_model.generate(input_ids, max_length=512, num_beams=4, length_penalty=2.0)

        # Decode the translated text
        translated_text = self.tokenizer.decode(translation_ids[0], skip_special_tokens=True)

        # Return the transferred linguistic information
        return {"translated_text": translated_text}
# def main():
#     # Provide the model name (Hugging Face model identifier)
#     model_name = "Helsinki-NLP/opus-mt-en-fr"

#     # Instantiate the OpenNMTTransferModule
#     transfer_module = OpenNMTTransferModule(model_name)

#     # Example analysis result (replace this with real linguistic information)
#     analysis_result = {
#         "text_to_translate": "Hello, how are you?",
#         "source_language": "en",
#         "target_language": "fr"
#     }

#     # Use the transfer module to perform language transfer
#     transferred_info = transfer_module.transfer(analysis_result)

#     # Display the results
#     print("Original Text:", analysis_result["text_to_translate"])
#     print("Translated Text:", transferred_info["translated_text"])

# if __name__ == "__main__":
#     main()
