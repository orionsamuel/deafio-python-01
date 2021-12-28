# deafio-python-01

O arquivo balanceamento.py é responsável por simular a carga de tarefas em servidores. O programa recebe como entrada um arquivo com a quantidade de ticks que cada tarefa tem,
a quantidade de usuários que cabem em um servidor e os usuários a se conctarem em um determinado instante de tempo. A saída é um arquivo com os servidores ativos em um dado
instante de tempo, além do custo total pelo uso dos servidores. Para executar o programa deve-se executar o comando python (python3) balanceamento.py no terminal.

O arquivo test_balanceamento.py contém funções de testes unitários para diversos casos do arquivo balanceamento.py. Esses testes são realizados através do framework Pytest que
 está instalado no ambiente virtual. Para executar o programa de teste deve executar o seguinte comando no terminal: pytest test_balanceamento.py.
