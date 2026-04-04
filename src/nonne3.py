from collections import deque
from llama_cpp import Llama
import json

class Nonne3:
    def __init__(self, model_path, config_path):
        with open(config_path) as f:
            config = json.load(f)
        self.llm = Llama(
            model_path=model_path,
            n_ctx=config["context_size"],
            verbose=False
        )

    def prep__prompt(self, system_prompt, history, user_input):
        prompt_lines = list(history)
        if not history or system_prompt not in history[0]:
            prompt_lines.insert(0, system_prompt)
        prompt_lines.append(f"<|im_end_9f3aXQ|>: {user_input}")
        prompt_lines.append("<|im_start_9f3aXQ|>:")
        return "\n".join(prompt_lines)

    def prompt(self, prompt, max_tokens=512, stream=True):
        output_text = ""
        for chunk in self.llm.create_completion(
            prompt,
            max_tokens=max_tokens,
            stream=stream,
            stop=["<|im_end_9f3aXQ|>"]
        ):
            text = chunk["choices"][0]["text"]
            if stream:
                print(text, end="", flush=True)
            output_text += text
        if stream:
            print()
        return output_text.strip()