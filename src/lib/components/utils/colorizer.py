import tkinter as tk


def search(text_widget, keyword, tag):
    pos = 1.0
    while True:
        # Note: In standard Tkinter, this is usually tk.END,
        # but the author uses bare 'END' here. Ensure 'END' is defined
        idx = text_widget.search(keyword, pos, tk.END)
        if not idx:
            break

        # Calculate the end position of the matched keyword
        pos = '{}+{}c'.format(idx, len(keyword))

        # Apply the styling tag to the matched text
        text_widget.tag_add(tag, idx, pos)
