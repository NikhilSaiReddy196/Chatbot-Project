from huggingface_hub import InferenceClient

def bot(prompt, hf_token) :
    
    client = InferenceClient(
        model = "mistralai/Mistral-7B-Instruct-v0.3",
        token = hf_token
    )
     
    message = [
        {"role" : "system", "content" : "you are a helpfull assistant"},
        {"role" : "user", "content" : prompt}
    ]

    responce = client.chat_completion(messages= message)

    return responce.choices[0].message.content.strip()
