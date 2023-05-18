from os import path
from bardcoder import BardCoder,traceback,json


if __name__ == "__main__":
    try:
        # set your input text
        prompt = input("Prompt: ")
        bard_coder = BardCoder(prompt,enable_logs=True)
        
        # Get the code from the response.
        code = bard_coder.get_code()
        
        filename = path.join("codes","code_generated")
        # Save the code to file
        bard_coder.save_code(filename,code)
        print(f"Code saved to file {filename}")
        
        # Save all the code choices to file
        bard_coder.save_code_choices("code_choice")
        
        # Print the links
        links = bard_coder.get_links()
        if links:
            print(f"Links: {links}")
            
        # Run all the code and code choices.
        bard_coder.run_code_choices()
    except Exception as e:
        # print the stack trace
        stack_trace = traceback.format_exc()
        print(stack_trace)
        print(str(e))
