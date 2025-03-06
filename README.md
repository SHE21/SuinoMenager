# Gerenciador de Granja de Suínos
![Captura de tela 2025-03-06 091545](https://github.com/user-attachments/assets/a4814b5c-f3ba-437f-8412-7c6afbd01bca)
![Captura de tela 2025-03-06 091611](https://github.com/user-attachments/assets/833b6be5-7b94-4e56-a1c9-0172441a0d1d)

## Descrição!

O **Gerenciador de Granja de Suínos** é um software desenvolvido para facilitar a administração de granjas, permitindo a visualização e controle das baias de porcos de forma interativa. O sistema inclui um mapa dinâmico das baias, com dimensões reais e capacidade de lotação, além da possibilidade de integração com sensores de temperatura e outras métricas em tempo real.

## Funcionalidades
- **Mapa Interativo da Granja**: Representação gráfica das baias com dimensões reais.
- **Capacidade de Lotação**: Cada baia exibe sua capacidade máxima de suínos.
- **Eventos Interativos**:
  - Clique nas baias para visualizar informações detalhadas.
  - Mudança de cor ao passar o cursor sobre uma baia.
  - Alteração da cor ao clicar para indicar seleção.
- **Personalização**:
  - Atualização das dimensões e cores das baias.
  - Possibilidade de expansão para incluir novas funcionalidades, como movimentação e redimensionamento das baias.
- **Integração com Sensores** (futuro): Monitoramento em tempo real de temperatura e outras variáveis ambientais dentro das baias.

## Tecnologias Utilizadas
- **Python 3**
- **PyQt5** para a interface gráfica e renderização das baias

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-granja.git
   cd gerenciador-granja
   ```
2. Instale as dependências:
   ```bash
   pip install PyQt5
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

## Como Usar
- **Visualização**: Abra o programa para ver a planta baixa da granja com as baias.
- **Interação**: Clique sobre uma baia para exibir detalhes no console.
- **Personalização**: Altere dimensões e cores das baias conforme necessário.

## Próximos Passos
- Implementação de um sistema de banco de dados para armazenar informações das baias.
- Integração com sensores para exibição de dados em tempo real.
- Interface para configuração dinâmica das baias pelo usuário.

## Contribuição
Sinta-se à vontade para contribuir com melhorias! Para isso:
1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Faça commit das suas mudanças:
   ```bash
   git commit -m "Adiciona nova funcionalidade X"
   ```
4. Envie um **pull request** para revisão.

## Licença
Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
