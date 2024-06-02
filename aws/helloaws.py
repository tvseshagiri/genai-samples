# generate code for call AWS bedrock API call for text generation

import json
import boto3
from botocore.exceptions import ClientError


class AWSBedrockTextGenerator:
    def __init__(self, region_name="ap-south-1"):
        self.bedrock_runtime_client = boto3.client(
            "bedrock-runtime", region_name=region_name
        )

    def invoke_mistral_7b(self, prompt):
        """
        Invokes the Mistral 7B model to run an inference using the input
        provided in the request body.

        :param prompt: The prompt that you want Mistral to complete.
        :return: List of inference responses from the model.
        """
        try:
            # Embed the message in Llama 3's prompt format.
            prompt = f"""
            <|begin_of_text|>
            <|start_header_id|>user<|end_header_id|>
            Write a brief about Generative AI in 10 lines.
            <|eot_id|>
            <|start_header_id|>assistant<|end_header_id|>
            """

            # Format the request payload using the model's native structure.
            request = {
                "prompt": prompt,
                # Optional inference parameters:
                "max_gen_len": 512,
                "temperature": 0.5,
                "top_p": 0.9,
            }

            model_id = "meta.llama3-70b-instruct-v1:0"

            response = self.bedrock_runtime_client.invoke_model(
                modelId=model_id, body=json.dumps(request)
            )

            response_body = json.loads(response["body"].read())

            response_text = response_body["generation"]

            return response_text

        except ClientError:
            print("Couldn't invoke Mistral 7B")
            raise


# Example usage
text_generator = AWSBedrockTextGenerator()
prompt = "Once upon a time, there was a magical kingdom where..."
generated_text = text_generator.invoke_mistral_7b(prompt)
print(f"Generated text: {generated_text}")
