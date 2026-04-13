echo "# Sistema de Acesso RFID com Arduino, Django e SQLite" > README.md
echo "" >> README.md
echo "## Descrição" >> README.md
echo "Sistema que lê cartões RFID usando Arduino e módulo RC522, envia os UIDs pela porta serial, e um script Python salva as leituras em um banco SQLite via Django. Uma interface web exibe os registros." >> README.md
echo "" >> README.md
echo "## Como executar localmente" >> README.md
echo "1. Clone o repositório" >> README.md
echo "2. Crie um ambiente virtual: \`python -m venv venv\`" >> README.md
echo "3. Ative: \`venv\\Scripts\\activate\` (Windows)" >> README.md
echo "4. Instale dependências: \`pip install -r requirements.txt\`" >> README.md
echo "5. Execute as migrações: \`python manage.py migrate\`" >> README.md
echo "6. Rode o servidor: \`python manage.py runserver\`" >> README.md
echo "7. Em outro terminal, execute \`python leitor_serial.py\` (ajuste a porta COM)" >> README.md
