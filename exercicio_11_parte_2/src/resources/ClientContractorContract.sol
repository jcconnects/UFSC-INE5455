pragma solidity 0.8.0;

contract ClientContractorContract {

    address owner = msg.sender; //dono do contrato é o criador

    enum Status { Created, InEffect, SuccessfulTermination, UnsuccessfulTermination }

    Status status;

    string client;
    string contractor;
    int creationDate;

    struct Obligation {
        bool exists;
        bool activated;
    }

    mapping(string => Obligation) obligations;

    constructor( string memory _client, string memory _contractor, int _creationDate ) public {
        client = _client;
        contractor = _contractor;
        creationDate = _creationDate;
        status = Status.Created;
    }

    //SETTERS

    function addObligation(string memory _id) public {
        obligations[_id] = Obligation(true, false);
    }

    function activate () public {
        status = Status.InEffect;
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

    function obligationExists(string memory _id) public view returns (bool) {
        return obligations[_id].exists;
    }

    function isObligationActivated(string memory _id) public view returns (bool) {
        return obligations[_id].activated;
    }

}
