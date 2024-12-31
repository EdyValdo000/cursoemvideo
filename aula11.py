# \033[0;30;41m fundo vermelho fonte branca
# \033[0;30;42m fundo verde fonte branca
# \033[7;30m fundo branco e cor preta
print('\033[0;30;41mOlá mundo\033[m')
print('\033[0;30;42mOlá mundo\033[m')
print('\033[7;30mOlá mundo\033[m')

ansi_codes = {
    "text": {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[39m"
    },
    "background": {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
        "reset": "\033[49m"
    },
    "style": {
        "bold": "\033[1m",
        "italic": "\033[3m",
        "underline": "\033[4m",
        "strikethrough": "\033[9m",
        "reset": "\033[0m"
    }
}

# Exemplo de uso
print(f"{ansi_codes['text']['yellow']}{ansi_codes['background']['blue']}{ansi_codes['style']['bold']}Texto amarelo com fundo azul e negrito{ansi_codes['style']['reset']}")
