import CRUD_produto

def test_adicionar_produtos():
    for y in range(1,3):
        entrada1=["aaa","2","5","1","agua","1"]
        resultado1=100+y
        assert CRUD_produto.adicionar_produto(entrada1)==resultado1

def test_atualizar():
    for x in range(1,3):
        entrada4=x
        entrada3=100+x
        entrada5=7
        resultado2=True
        assert CRUD_produto.atualizar_produtos(entrada3, entrada4, entrada5)==resultado2
    entrada4=3
    entrada3=101
    entrada5="bolo"
    assert CRUD_produto.atualizar_produtos(entrada3, entrada4, entrada5)==resultado2
    
def test_pesquisar():
    entrada6="bolo"
    resultado4=['ID: 101 - R$7 - bolo - 2 em estoque']
    assert CRUD_produto.buscar_produto(entrada6)==resultado4

def test_deletar_produto():
    for z in range(1,3):
        entrada2=100+z
        resultado3=True
        assert CRUD_produto.deletar_produto(entrada2)==resultado3

def test_lista_tudo():
    resultado6=["ID: 1 - R$250 - Fone Bluetooth Elite - Fone de ouvido com cancelamento de ruído ativo - 50 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",   
"ID: 2 - R$25 - Capinha Protetora X - Capinha silicone resistente a impactos - 100 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 3 - R$180 - Caixa Som Bluetooth Pro - Caixa de som portátil à prova d'água - 30 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 4 - R$15 - Película Vidro 3D - Película de vidro temperado 9H - 200 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 5 - R$40 - Carregador Turbo - Carregador rápido 20W PD - 80 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 6 - R$120 - Fone Esportivo Fit - Fone de ouvido esportivo à prova d'água - 60 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 7 - R$20 - Capinha Ultra Slim - Capinha transparente com design slim - 150 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 8 - R$220 - Caixa Som Party - Caixa de som com luzes LED - 25 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 9 - R$12 - Película Hidrogel - Película hidrogel anti-riscos - 180 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 10 - R$80 - Carregador Sem Fio - Carregador wireless 15W - 45 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 11 - R$300 - Fone True Wireless - Fone de ouvido com estojo de carga - 70 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 12 - R$60 - Capinha Couro Elegant - Capinha couro genuíno - 40 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 13 - R$100 - Caixa Som Mini - Caixa de som mini portátil - 90 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 14 - R$18 - Película Matte - Película matte anti-reflexo - 120 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 15 - R$35 - Carregador Carro - Carregador veicular 30W - 55 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 16 - R$400 - Fone Studio Pro - Fone de ouvido over-ear com áudio surround - 20 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 17 - R$30 - Capinha Bumper - Capinha bumper com suporte - 110 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 18 - R$150 - Caixa Som Outdoor - Caixa de som rugged à prova de choque - 35 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 19 - R$22 - Película Privacidade - Película privacidade 360° - 95 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 20 - R$120 - Power Bank Turbo - Carregador portátil 10000mAh - 60 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 21 - R$180 - Fone Call Pro - Fone de ouvido com mic cancelamento de ruído - 85 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 22 - R$28 - Capinha Glitter - Capinha glitter personalizável - 75 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 23 - R$320 - Caixa Som Smart - Caixa de som com assistente virtual - 15 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 24 - R$20 - Película Full Cover - Película curva completa - 130 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 25 - R$25 - Cabo USB-C Turbo - Cabo USB-C 2m rápido - 200 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 26 - R$90 - Fone Bass Pro - Fone de ouvido bass boost - 45 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 27 - R$35 - Capinha Premium - Capinha capa dura com impressão - 65 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 28 - R$200 - Caixa Som Stereo - Caixa de som stereo dual - 40 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 29 - R$16 - Película Nano - Película nano anti-bacteriana - 140 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 30 - R$65 - Carregador Dual - Carregador dual port 45W - 50 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 31 - R$220 - Fone Gaming Pro - Fone de ouvido gaming RGB - 30 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 32 - R$18 - Capinha Grip - Capinha silicone texturizada - 160 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 33 - R$85 - Caixa Som Compact - Caixa de som compacta - 70 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 34 - R$24 - Película 4D Glass - Película glass 4D - 110 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 35 - R$75 - Carregador Magnetic - Carregador magnético wireless - 40 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 36 - R$110 - Fone Neckband - Fone de ouvido neckband - 55 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 37 - R$32 - Capinha Ring - Capinha com anel suporte - 85 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 38 - R$180 - Caixa Som Power - Caixa de som com powerbank - 25 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 39 - R$28 - Película SpyGuard - Película anti-espionagem - 100 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 40 - R$20 - Cabo Lightning - Cabo Lightning 1m - 180 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 41 - R$150 - Fone Retro - Fone de ouvido retro - 15 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 42 - R$15 - Capinha Color - Capinha transparente colorida - 135 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 43 - R$280 - Caixa Som Float - Caixa de som flutuante - 10 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 44 - R$30 - Película Self-Heal - Película self-healing - 90 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 45 - R$95 - Carregador Stand - Carregador wireless stand - 35 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 46 - R$270 - Fone ANC Pro - Fone de ouvido com ANC - 50 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 47 - R$40 - Capinha Military - Capinha militar resistente - 70 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 48 - R$240 - Caixa Som Karaoke - Caixa de som com karaokê - 20 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 49 - R$19 - Película Curved - Película curved edge - 125 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 50 - R$110 - Carregador GaN - Carregador GaN 65W - 30 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 51 - R$130 - Fone Sport Wireless - Fone de ouvido esportivo wireless - 65 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 52 - R$55 - Capinha Book - Capinha book estilo carteira - 45 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 53 - R$160 - Caixa Som Shower - Caixa de som showerproof - 40 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 54 - R$21 - Película Blue Light - Película anti-blue light - 155 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 55 - R$200 - Carregador Solar - Carregador solar portátil - 15 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 56 - R$190 - Fone Stylus - Fone de ouvido com estilete - 25 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 57 - R$38 - Capinha Stand - Capinha com pedestal - 80 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 58 - R$120 - Caixa Som Mini Rug - Caixa de som mini rugged - 60 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 59 - R$17 - Película Anti-Finger - Película matte anti-fingerprint - 140 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 60 - R$85 - Carregador Duo - Carregador wireless duo - 50 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 61 - R$350 - Fone Translator - Fone de ouvido com tradução - 10 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 62 - R$14 - Capinha Sticky - Capinha silicone adesiva - 170 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 63 - R$95 - Caixa Som Alarm - Caixa de som com alarme - 35 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 64 - R$26 - Película Full Glue - Película 9H full glue - 115 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 65 - R$22 - Cabo Angled - Cabo USB-C 90° angled - 145 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 66 - R$160 - Fone Open-Ear - Fone de ouvido open-ear - 40 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 67 - R$70 - Capinha Zoom - Capinha com lente zoom - 20 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 68 - R$110 - Caixa Som FM - Caixa de som com FM radio - 55 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 69 - R$29 - Película Privacy Glass - Película privacy glass - 105 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 70 - R$78 - Carregador Car Mount - Carregador wireless car mount - 40 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 71 - R$240 - Fone Health - Fone de ouvido com heart rate - 30 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 72 - R$33 - Capinha Eco - Capinha eco-friendly biodegradável - 90 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 73 - R$300 - Caixa Som 360 - Caixa de som 360° sound - 25 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 74 - R$23 - Película Anti-Glare - Película anti-glare - 135 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 75 - R$120 - Carregador Dock - Carregador desk dock - 35 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 76 - R$180 - Fone Modular - Fone de ouvido modular - 50 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 77 - R$150 - Capinha Smart - Capinha com tela integrada - 15 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 78 - R$140 - Caixa Som Slim - Caixa de som ultra-slim - 60 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 79 - R$18 - Película Anti-Smudge - Película matte anti-smudge - 160 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 80 - R$90 - Carregador Pad - Carregador wireless power pad - 45 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 81 - R$290 - Fone Gesture - Fone de ouvido com gesture control - 35 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 82 - R$42 - Capinha Anti-Theft - Capinha anti-roubo - 75 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 83 - R$170 - Caixa Som EQ - Caixa de som com equalizer - 40 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 84 - R$31 - Película Crystal - Película liquid crystal - 110 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 85 - R$70 - Carregador Fast Wireless - Carregador wireless fast charge - 55 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 86 - R$210 - Fone Noise Cancel - Fone de ouvido com noise canceling - 60 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 87 - R$80 - Capinha Cooler - Capinha com cooler integrado - 25 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 88 - R$130 - Caixa Som Vintage - Caixa de som vintage style - 30 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 89 - R$19 - Película Anti-Static - Película anti-static - 140 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 90 - R$150 - Carregador Multi - Carregador multi-port 100W - 20 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 91 - R$100 - Fone Sport Neck - Fone de ouvido esportivo neckband - 70 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 92 - R$45 - Capinha Storage - Capinha com armazenamento - 50 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 93 - R$190 - Caixa Som App - Caixa de som com app control - 35 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 94 - R$27 - Película Nano Glass - Película nano glass - 125 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 95 - R$88 - Carregador Magnetic Stand - Carregador wireless magnetic stand - 40 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1",
"ID: 96 - R$320 - Fone Spatial - Fone de ouvido com spatial audio - 25 em estoque - ID de categoria: 1 - Registrado pelo úsuario de ID: 1",
"ID: 97 - R$37 - Capinha Pen Holder - Capinha com suporte para caneta - 65 em estoque - ID de categoria: 2 - Registrado pelo úsuario de ID: 1",
"ID: 98 - R$400 - Caixa Som Levitation - Caixa de som flutuante levitation - 10 em estoque - ID de categoria: 3 - Registrado pelo úsuario de ID: 1",
"ID: 99 - R$25 - Película Antimicrobial - Película anti-microbial - 155 em estoque - ID de categoria: 4 - Registrado pelo úsuario de ID: 1",
"ID: 100 - R$130 - Carregador Box - Carregador wireless charging box - 30 em estoque - ID de categoria: 5 - Registrado pelo úsuario de ID: 1"]
    assert CRUD_produto.listar_todos()==resultado6

def test_estoque_baixo():
    resultado7=["Caixa Som Party - tem 25 em estoque!",
"Fone Studio Pro - tem 20 em estoque!",
"Caixa Som Smart - tem 15 em estoque!",
"Caixa Som Power - tem 25 em estoque!",
"Fone Retro - tem 15 em estoque!",
"Caixa Som Float - tem 10 em estoque!",
"Caixa Som Karaoke - tem 20 em estoque!",
"Carregador Solar - tem 15 em estoque!",
"Fone Stylus - tem 25 em estoque!",
"Fone Translator - tem 10 em estoque!",
"Capinha Zoom - tem 20 em estoque!",
"Caixa Som 360 - tem 25 em estoque!",
"Capinha Smart - tem 15 em estoque!",
"Capinha Cooler - tem 25 em estoque!",
"Carregador Multi - tem 20 em estoque!",
"Fone Spatial - tem 25 em estoque!",
"Caixa Som Levitation - tem 10 em estoque!"]
    assert CRUD_produto.baixo_estoque()==resultado7

def testando_estoque_alto():
    resultado8=["Película Vidro 3D - tem 200 em estoque!",
"Capinha Ultra Slim - tem 150 em estoque!",
"Película Hidrogel - tem 180 em estoque!",
"Película Matte - tem 120 em estoque!",
"Capinha Bumper - tem 110 em estoque!",
"Película Full Cover - tem 130 em estoque!",
"Cabo USB-C Turbo - tem 200 em estoque!",
"Película Nano - tem 140 em estoque!",
"Capinha Grip - tem 160 em estoque!",
"Película 4D Glass - tem 110 em estoque!",
"Cabo Lightning - tem 180 em estoque!",
"Capinha Color - tem 135 em estoque!",
"Película Curved - tem 125 em estoque!",
"Película Blue Light - tem 155 em estoque!",
"Película Anti-Finger - tem 140 em estoque!",
"Capinha Sticky - tem 170 em estoque!",
"Película Full Glue - tem 115 em estoque!",
"Cabo Angled - tem 145 em estoque!",
"Película Privacy Glass - tem 105 em estoque!",
"Película Anti-Glare - tem 135 em estoque!",
"Película Anti-Smudge - tem 160 em estoque!",
"Película Crystal - tem 110 em estoque!",
"Película Anti-Static - tem 140 em estoque!",
"Película Nano Glass - tem 125 em estoque!",
"Película Antimicrobial - tem 155 em estoque!"]
    assert CRUD_produto.alto_estoque()==resultado8