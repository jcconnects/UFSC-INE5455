pragma solidity 0.8.0;

contract ClientContractorContract {

    address owner = msg.sender; //dono do contrato é o criador

    enum Status { Created, InEffect, SuccessfulTermination, UnsuccessfulTermination }

    Status status;

    string client;
    string contractor;
    int creationDate;

    // Obrigações essenciais para o encerramento bem-sucedido
    bool servicesProvided;
    bool firstHalfPaid;
    bool secondHalfPaid;

    constructor( string memory _client, string memory _contractor, int _creationDate ) public {
        client = _client;
        contractor = _contractor;
        creationDate = _creationDate;
        status = Status.Created;
    }

    //SETTERS

    function activate () public {
        status = Status.InEffect;
    }

    // A contratada presta os serviços contratados
    function provideServices() public {
        servicesProvided = true;
        evaluateTermination();
    }

    // A contratante paga metade do serviço na assinatura do contrato
    function payFirstHalf() public {
        firstHalfPaid = true;
        evaluateTermination();
    }

    // A contratante paga a outra metade trinta dias após o início dos trabalhos
    function paySecondHalf() public {
        secondHalfPaid = true;
        evaluateTermination();
    }

    // Encerramento bem-sucedido quando todas as obrigações essenciais foram cumpridas
    function evaluateTermination() private {
        if ((servicesProvided) && (firstHalfPaid) && (secondHalfPaid)) {
            status = Status.SuccessfulTermination;
        }
    }

    // Uma obrigação essencial não foi cumprida: encerramento malsucedido
    function breach() public {
        status = Status.UnsuccessfulTermination;
    }

    //GETTERS

    //view significa que nao tem transacao, nao precisa minerar (nao usa gas para executar)

    function getStatus() public view returns (Status) {
        return status;
    }

    function isActivated() public view returns (bool) {
        return status == Status.InEffect;
    }

    function getClient() public view returns (string memory) {
        return client;
    }

    function getCreationDate() public view returns (int) {
        return creationDate;
    }

}
