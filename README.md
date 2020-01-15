# Trello Python Parser

I have one need. And maybe others can have the same.
I need to have a hierarchical representation of a Trello board, for many reasons: 
- I want to version it on another system
- I have to share it within a legacy system
- I must print all the cards of a board
- ...

Trello, since v1, exposes different ways to export cards but in the free plan, only a JSON representation of a board is allowed. 
But.. we are programmer, it is more than enough.
Hence, a simple Python script able to take a trello.json file and to transform to a hierarchical markdown file

# Notes

All the markdown customizazions and Parser functionalities are made for my own purposes. 
Do you want to contrinute? PR are more than welcome, expecially because I am not a Python programmer and so.. I can learn :)


# Tools
- markdown viewer: http://markdown-it.github.io/
- json editor: https://jsonformatter.org/json-parser