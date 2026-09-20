import requests
import json
import sys




LM_STUDIO_URL = "http://localhost:1234/v1"

model_selected = ""

def query_available_lm():
    try:
        idlist = []
        response = requests.get(LM_STUDIO_URL+"/models").json()
        resp = response.get('data')
        for r in resp:
            
            idlist.append(r.get('id'))
        return idlist
    except:
        print("Error: Ensure LMstudio is running and server is selected!")
        return []

def model_selector():
    number = 1
    model = ""
    modellist = query_available_lm()
    for list in modellist:
        
        print(str(number)+ " " + list)
        number = number+1
    if not model:
        print("Please select a models number from the above list:")
        model_number = input()
        model_num = int(model_number)-1
        model = modellist[model_num]


    return model




def chat_with_lm_studio(user_message, conversation_history):
    """
    Sends a message to LM Studio and returns the response.
    """
    payload = {
        "model": model_selected, # If empty, LM Studio uses the loaded model
        "messages": conversation_history + [{"role": "user", "content": user_message}],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }

    try:
        response = requests.post(LM_STUDIO_URL+"/chat/completions", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Connection Error: Make sure LM Studio server is running. Details: {e}"

def main_chat_loop():
        x = True;
    # 2. Conversation Memory
        # We start with a system prompt to tell the AI how to act
        conversation_history = [
            {"role": "system", "content": "You are a helpful and intelligent assistant."}
        ]
    
        print("Type 'quit' or 'exit' to stop.")
        
        while x:
            user_input = input("\nYou: ")
    
            
                
    
            # 3. Get AI Response
            print("\nAI: ", end="", flush=True)
            response_text = chat_with_lm_studio(user_input, conversation_history)
            print(response_text)
    
            # 4. Update History
            # It is crucial to add the user's message AND the AI's response to the history
            # so the AI remembers the context of the conversation.
            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "assistant", "content": response_text})
            if user_input.lower() in ["quit", "exit"]:


                x = False;
                print("Closing connection. Goodbye!")
        return 0

def download_models():
    print("Please type the URL(from huggingface) of the model you wish to download: ")
    new_model = input()
    response = requests.post((LM_STUDIO_URL+"/models/download"), new_model)
    return response

def main():
    global model_selected
    print("="*50)
    print("   LM Studio Local Chat Client")
    print("="*50)
    while True:
        print("Please select an option \n1.Select a model \n2.chat with a model \n3.Download a model \nor exit:")
        userin = input()
        match userin:
            case "1":
                print("one selected")
                model_selected = model_selector()
            case "2":
                main_chat_loop()
            case "3":
                resp = download_models()
                print(resp)
            case _:
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()


