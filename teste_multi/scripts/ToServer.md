JsonFunctions = [
    {
        "name": "Algoritmo MoveBase",
        "api_name": "self.BotMoveBase",
        "description": "Algoritmo de planejamento de trajeto para movimento de robôs. Esta função calcula o trajeto para um robô específico alcançar um objetivo designado.",
        "parameters": [
            {
                "name": "meta",
                "enum": ["cozinha", "garagem", "quarto A", "quarto B", "seção A", "seção B", "sala de estar", "banheiro"],
                "description": "O local para onde o robô precisa ir. As opções disponíveis incluem: cozinha, garagem, quarto A, quarto B, seção A, seção B, sala de estar e banheiro."
            },
            {
                "name": "ID",
                "description": "O número do robô, que é um identificador único atribuído ao robô. Este ID é usado para especificar qual robô precisa realizar o planejamento de trajeto."
            }
         ]
    }
]

