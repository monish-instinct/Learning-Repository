from taipy.gui import Gui

content = ''
img_path = 'logo.png'

index = f"""
<|text-center|
<h1>Hello</h1>
    <|{img_path}|image|>
    <|{content}|file_selector|>
    Select an Image
>
"""

app = Gui(page=index)

def update_content(file_path):
    global content
    content = file_path
    print(f"Selected file: {content}")
    app.update_page()

if __name__ == '__main__':
    app.run(use_reloader=True, port=5001)
