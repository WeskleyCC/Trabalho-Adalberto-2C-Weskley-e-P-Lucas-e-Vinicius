
listm = [{"nomem": "Pedro", "cpfm": "12345678910", "rgm": "1", "crmm": "1", "telm": "23203203", "endm": "Rua da silva", "sexom": "M", "senha": "abc"}]
listp = [{"nomep": "Adailto", "endp": "Juremal", "telp": "40028922", "cpfp": "1114321", "rg": "44", "sexop": "M", "covp": "casa dele"}]
listc = [{"nomec": "Plano", "telc": "0000010", "endc": "Ali", "cnpj": "101010", "plan": "sim"}]
compromisso = [{"Data": "", "Hora Inicial": "", "Hora Final": "", "Descrição": ""}]
consultas = [{"Médico": "Pedro", "Paciente": "Adailto", "Data": "Amanhã", "Hora": "10h"}]
x = True
while x:
    lang = input("1 - Cadastrar Médicos\n"
             "2 - Cadastrar Pacientes\n"
             "3 - Cadastrar Convênios\n"
             "4 - Buscar Médicos\n"
             "5 - Buscar Pacientes\n"
             "6 - Buscar Convênios\n"
             "7 - Alterar Medicos\n"
             "8 - Alterar Pacientes\n"
             "9 - Marcar Compromisso\n"
             "10 - Marcar Consulta\n"
             "11 - Emitir Relatorio\n"
             "12 - Encerrar Programa\n"
             "O que você deseja fazer? ")
    
    def cadastrarMedicos():
        nomem = input("insira seu nome: ")
        cpfm = int(input("insira seu cpf: "))
        rgm = int(input("insira seu rg: "))
        crmm = int(input("insira seu crm: "))
        telm = int(input("insira seu telefone: "))
        endm = input("insira seu endereço: ")
        sexom = input("qual seu sexo? ")
        senha = input("diga sua senha? ")
        
        
        listm.append({
         "nomem": nomem,
         "cpfm": cpfm,
         "crmm": crmm,
         "rgm": rgm,
         "telm": telm,
         "endm":  endm,
         "sexom": sexom,
         "senha": senha})
        
        print("o médico ",nomem," foi cadastrado!")

    def cadastrarPacientes():
            nomep = input("insira seu nome: ") 
            endp = input("insira seu endereço: ")
            telp = int(input("insira seu telefone: "))
            cpfp = int(input("insira seu cpf: "))
            rg = int(input("insira seu rg: "))
            sexop = input("qual seu sexo? ")
            covp = input("qual o seu covênio? ")
            
              
            
            listp.append({
        "nomep": nomep, 
        "cpfp": cpfp,
        "rg": rg,
        "telp": telp,
        "endp": endp,
        "sexop": sexop,
        "covp": covp })
            
            print("o paciente ",nomep," foi cadastrado!")
              
            

    def cadastrarConvenios():
        nomec = input("insira seu nome: ")
        telc = int(input("insira seu telefone: "))
        endc = input("insira seu endereço: ")
        cnpj = int(input("insira seu cnpj: "))
        plan = input("Quais os planos oferecidos pelo covênio? ")
        

        listc.append({
        "nomec": nomec,
        "telc": telc,
        "endc": endc,
        "cnpj": cnpj,
        "plan": plan}) 

        print("O covênio ",nomec ," foi cadastrado!")

    def buscarmedicos():
        buscm = input("Digite o Nome ou o CRM do médico que deseja buscar: ")
        for medico in listm:
                if medico["nomem"] == buscm or medico["crmm"] == int(buscm):
                    print("Médico encontrado!")
                    print("Nome:", medico["nomem"])
                    print("Telefone:", medico["telm"])
                    return medico
        print("Médico nao encontrado!")  

    def buscarPacientes():
        buscp = input("Digite o nome ou cpf do paciente: ")
        for paciente in listp:
                  if paciente["nomep"] == buscp or paciente["cpfp"] == int(buscp):
                    print("Paciente encontrado!")
                    print("pacienteCPF:", paciente["cpfp"])
                    print("pacienteTelefone:", paciente["telp"])
                    return paciente
        print("Paciente não encontrado!") 

                     

    def buscarConvenios():
     buscc = input("Digite o cnpj ou nome do convenio: ")
     for convenio in listc:
         if convenio["cnpj"] == buscc or convenio["nomec"] == buscc:
             print("Convenio encontrado!")
             print("convenioNome:", convenio["nomec"])
             print("convenioTelefone:", convenio["telc"])
             print("convenioCNPJ:", convenio["cnpj"])
             return
     print("Convenio não encontrado!")

             
    
    def alterarMedicos():
     nomem = input("Digite o nome do médico: ")
     for medico in listm:
         if medico["nomem"] == nomem:
            medico["cpfm"] = input("Digite o novo cpf do médico: ")
            medico["crmm"] = input("Digite o novo CRM do médico: ")
            medico["rgm"] = input("Digite o novo RG do médico: ")
            medico["telm"] = input("Digite o novo telefone do médico: ")
            medico["endm"] = input("Digite o novo endereço do médico: ")
            print("Médico mudado com sucesso!")
            return
     print("Médico não encontrado!")
                               
    def alterarPacientes():
     nomep = input("Digite o nome do paciente: ")
     for paciente in listp:
         if  paciente["nomep"] == nomep:
             paciente["cpfp"] = input("Digite o novo cpf do paciente: ")
             paciente["rgp"] = input("Digite o novo RG do paciente: ")
             paciente["telp"] = input("Digite o novo telefone do paciente: ")
             paciente["endp"] = input("Digite o novo endereço do paciente: ")
             paciente["convenio"] = input("Digite o novo convenio que o paciente está relacionado: ")
             print("Paciente alterado com sucesso!")
             return
     print("Paciente não encontrado!")
                                    
    def marcarCompromisso():
        if not compromisso:
            return
        data = input("Escolha uma data: ")
        horai = input("Escolha a hora de inicio: ")
        horaf = input("Diga a hora de termino: ")
        descricao = input("Descreva seu compromisso: ")

        compromisso.append({
            "data" : data,
            "horai" : horai,
            "horaf" : horaf,
            "descricao" : descricao
        })
        print("Compromisso marcado com sucesso")
        
            
    def marcarConsulta():
        medicoC = ""
        pacienteC = ""
        
        escolhaM = int(input("Você quer buscar médicos por nome ou CRM?\nDigite 1 para nome e 2 para CRM: "))
        while escolhaM < 1 or escolhaM > 2:
            escolhaM = int(input("Escolha inválida. Tente novamente."))
        
        if escolhaM == 1:
            buscaMedico = input("Digite o nome do médico: ")
            for n in listm:
                if n["nomem"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("nomem:", n["nomem"], "\ntelm:", n["telm"], "\ncrmm:", n["crmm"])
                    consultaM = int(input("Você deseja escolher este médico?\nDigite 1 para sim ou 2 para não: "))
                    if consultaM == 1:
                        medicoC = n["nomem"] 
                    if consultaM == 2:
                        print()
        
        if escolhaM == 2:
            buscaMedico = input("Digite o CRM do médico: ")
            for n in listm:
                if n["crmm"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("nomem:", n["nomem"], "\ntelm:", n["telm"], "\ncrmm:", n["crmm"])
                    consultaM = int(input("Você deseja escolher este médico?\nDigite 1 para sim ou 2 para não: "))
                    if consultaM == 1:
                        medicoC = n["nomem"]
                    if consultaM == 2:
                        print()
        
        escolhaP = int(input("Você quer buscar paciente por nome ou CPF?\nDigite 1 para nome e 2 para CPF: "))
        while escolhaP < 1 or escolhaP > 2:
            escolhaP = int(input("Escolha inválida. Tente novamente."))
        if escolhaP == 1:
            buscaPaciente = input("Digite o nome do paciente: ")
            for n in listp:
                if n["nomep"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("nomep:", n["nomep"], "\ntelp:", n["telp"], "\ncpfp:", n["cpfp"])
                    consultaP = int(input("Você deseja escolher este paciente?\nDigite 1 para sim ou 2 para não: "))
                    if consultaP == 1:
                        pacienteC = n["nomep"]
                    if consultaP == 2:
                        print()
        if escolhaP == 2:
            buscaPaciente = input("Digite o CPF do pacientes: ")
            for n in listp:
                if n["cpfp"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("nomep:", n["nomep"], "\ntelp:", n["telp"], "\ncpfp:", n["cpfp"])
                    consultaP = int(input("Você deseja escolher este paciente?\nDigite 1 para sim ou 2 para não: "))
                    if consultaP == 1:
                        pacienteC = n["nomep"]
                    if consultaP == 2:
                        print()
        dataC = input("Digite o dia da consulta: ")
        horaC = input("Digite a hora completa da consulta: ")
        consultas.append({"Médico": medicoC, "Paciente": pacienteC, "Data": dataC, "Hora": horaC})
        print(f"Consulta marcada para às {horaC} do dia {dataC} com {pacienteC}, para o médico {medicoC}.")

       
    def emitirRelatorio():
        relatorios = int(input("Escolha o tipo de relatório:\nDigite 1 para médicos cadastrados;\n2 para pacientes cadasatrados;\n3 para convênios;\n4 para consultas: "))
        if relatorios == 1:
            print("Médicos cadastrados:")
            for n in listm:
                print(n["nomem"])
        
        if relatorios == 2:
            print("Pacientes cadastrados:")
            for n in listp:
                print(n["nomep"])
        
        if relatorios == 3:
            print("Convênios cadastrados:")
            for n in listc:
                print(n["nomec"])
        
        if relatorios == 4:
            print("Consultas marcadas:")
            for n in consultas:
                print(f"Dia: {n['Data']} \nHora: {n['Hora']}\n")
             
    match lang:
        case "1":
            cadastrarMedicos()
            
        

        case "2":
            cadastrarPacientes()
            

        case "3":
         cadastrarConvenios()
         
    
        case "4":
            buscarmedicos()
            

        case "5":
            buscarPacientes()
            
        
        case "6":
            buscarConvenios()
            

        case "7":
            alterarMedicos()
            

        case "8":
            alterarPacientes()
            
    
        case "9":
            marcarCompromisso()
           

        case "10":
            marcarConsulta()
            

        case "11":
            emitirRelatorio()
            
    
        case "12": 
              x = False
        case _:
            print("Escolha uma opção válida")
            
        