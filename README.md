# Scrappy-Bot-Coral
Scrappy boy using selenium get categories for a data base.

The code was created for study purposes and only saves the data already provided for the general public.

# How it works

The bot opens category by category at "https://www.armazemcoral.com.br" and stores the name, category and subcategory information of each product.

# Setting Up

You have to specify the number of lines and menu vocals on line 151 and 158. For the example site I used 22 and 2, but I tested it with 2 and 1 before to see how it works.

The excess of try and except is due to multiple different objects per page (if a page has only 20 products the XPATH is one, if it has 50 it changes...) I couldn't find a better way to do this check and I did it anyway . It works.


# Como funciona

O bot abre categoria por categoria no "https://www.armazemcoral.com.br" e guarda as informações de nome, categoria e subcategoria de cada produto.

# Configurando

Você tem que especificar o número de linhas e colunas do menu na linha 151 e 158. Para o site de exemplo foi usado 22 e 2, mas eu aconselho testar com 2 e 1 antes para ver como está o funcionamento.

O excesso de try e except é devido aos múltiplos objetos diferentes por pagina (caso uma página tenha apenas 20 produtos o XPATH é um, se tiver 50 já muda...) eu não achei uma forma melhor de fazer essa verificação e fiz assim mesmo. Funciona.


