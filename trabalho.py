import pandas as pd
import matplotlib.pyplot as plt

try:
    # Lendo o arquivo csv
    dados = pd.read_csv("./dados4.csv")

    # 1) Ajuste as idades que não são válidas ou estão vazias para a moda da amostra. Grave a saída no arquivo Resposta01.txt

    # Calculando a moda das idades
    moda_idade = dados["age"].mode().iloc[0]

    # Substituindo os valores inválidos ou vazios pela moda
    dados["age"] = dados["age"].fillna(moda_idade)

    # Salvando a resposta no arquivo Resposta01.txt
    dados.to_csv("Resposta01.txt", index=False)

    # 2) Apresente no terminal o somatório de homens (male) e de mulheres (female)

    # Calculando o total de Homens
    total_homens = dados[dados["sex"] == "male"].shape[0]

    # Calculando o total de Mulheres
    total_mulheres = dados[dados["sex"] == "female"].shape[0]

    print(f"Total de homens: {total_homens}")
    print(f"Total de mulheres: {total_mulheres}")

    # 3) Considerando a coluna "survived", sendo 0 como não sobrevivente e 1 como sobrevivente,
    # apresente em um gráfico de pizza a porcentagem de sobreviventes e não sobreviventes.

    # calculando a quantidade de sobreviventes e não sobreviventes
    sobreviventes = dados[dados["survived"] == 1].shape[0]
    nao_sobreviventes = dados[dados["survived"] == 0].shape[0]

    # preparando os dados para o gráfico de pizza
    labels = ["Sobreviventes", "Não Sobreviventes"]
    sizes = [sobreviventes, nao_sobreviventes]
    colors = ["lightgreen", "lightcoral"]
    explode = (0.1, 0)

    # criando o gráfico de pizza
    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )
    plt.axis("equal")
    plt.title("Porcentagem de sobreviventes e não sobreviventes")
    plt.savefig("grafico_pizza.png")

    # 4) Apresente o gráfico de dispersão da Idade pela tarifa.

    # criando o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(dados["age"], dados["fare"], color="blue", alpha=0.5)
    plt.title("Gráfico de Dispersão: Idade vs. Tarifa")
    plt.xlabel("Idade")
    plt.ylabel("Tarifa")
    plt.grid(True)
    plt.savefig("grafico_dispersao.png")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
