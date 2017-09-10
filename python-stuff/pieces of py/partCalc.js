$(document).ready(function () {

var s4Parts = {
    "Cabinet":[

        {"id": 1,
        "Desc":"Series 4 cabinet with Standard Capacity Bill Acceptors"},

        {"id": 2,
        "Desc":"Series 4 cabinet with Extended Capacity Bill Acceptors"},

        {"id": 3,
        "Desc":"Series 4 cabinet with hardened steel doors"},

        {"id": 4,
        "Desc":"Series 4 cabinet with hardened steel doors and Extended Capacity Cassettes"},

        {"id": 5,
        "Desc":"No Description Please check your part number"},

        {"id": 6,
        "Desc":"TACC-VI"}
    ],

    "AcceptorQTY":[
        {"id": 1,
        "Desc":"One"},

        {"id": 2,
        "Desc":"Two"}
    ],

    "Acceptors":[
        {"id": "S",
        "Name":"BILL ACCEPTOR HEAD, (MEI SINGLE NOTE FEEDER), USA",
        "PartNum": "644-0106-303S",
        "Desc":"MEI ADVANCED (increased acceptance speed)For 66mm notes"},

        {"id": "B",
        "Name":"BILL ACCEPTOR HEAD, (MEI BULK NOTE FEEDER), USA",
        "PartNum": "644-0117-434S",
        "Desc":"The bill tray snaps onto the bezel that is mounted on the front of the bill acceptor. For 66mm notes"},

        {"id": "NA",
        "Name":"BILL ACCEPTOR HEAD, (MEI SINGLE NOTE FEEDER), USA, RECONDITIONED",
        "PartNum": "644-0106-300R",
        "Desc":"For 66mm notes"}
    ],

    "ControlPCB":[
        {"id": 1,
        "Name":"PCB, CONTROL PANEL",
        "PartNum": "210-0240-104S",
        "Desc":"For customers with Brinks association only For Serial#'s below UG-07470 and UH-01900 Does Not include FlashCard. Control Panel PCB - Distribution PCB cable connection is a flat ribbon cable (SCSI type)"},

        {"id": 2,
        "Name":"PCB, CONTROL PANEL",
        "PartNum": "210-0320-104S",
        "Desc":"For Series 4 units only. For customers with Brinks association only For Serial#'s above UG-07470 and UH-01900 Does Not include FlashCard Control Panel PCB - Distribution PCB cabling has MTA type connectors. One end has 14 pin connector, opposite end has 11 and 4 pin connectors"},

        {"id": 3,
        "Name":"PCB, CONTROL PANEL",
        "PartNum": "210-0240-109S",
        "Desc":"For Series 4 units with add-on Storage Vault module For customers with Brinks association only For Serial#'s below UG-07470 and UH-01900Does Not include FlashCard For units equipped with a Storage Vault Control Panel PCB - Distribution PCB cable connection is a flat ribbon cable (SCSI type)"},

        {"id": 4,
        "Name":"PCB, CONTROL PANEL",
        "PartNum": "210-0320-109S",
        "Desc":"For Series 4 units with add-on Storage Vault module For customers with Brinks association only For Serial#'s above UG-07470 and UH-01900 Does Not include FlashCard For units equipped with a Storage Vault Control Panel PCB - Distribution PCB cabling has MTA type connectors. One end has 14 pin connector, opposite end has 11 and 4 pin connectors."},

        {"id": 5,
        "Name":"PCB, CONTROL PANEL",
        "PartNum": "210-0240-105S",
        "Desc":"For Series 4 units only. For customers with Loomis association only For Serial#'s below UG-07470 and UH-01900 Does Not include FlashCard Control Panel PCB - Distribution PCB cable connection is a flat ribbon cable (SCSI type)"},

        {"id": 6,
        "Name":"PCB, CONTROL PANEL",
        "PartNum": "210-0320-105S",
        "Desc":"For Series 4 units only. For customers with Loomis association only For Serial#'s above UG-07470 and UH-01900 Does Not include FlashCard Control Panel PCB - Distribution PCB cabling has MTA type connectors. One end has 14 pin connector, opposite end has 11 and 4 pin connectors"}
    ],

    "Printer":[
        {"id": 1,
        "Name":"PCB, PRINTER (KFI)",
        "PartNum": "644-0132-101S",
        "Desc":"Printer Control Board"},

        {"id": 2,
        "Name":"PRINTER, KFI INTEGRATED (BUILT-IN)",
        "PartNum": "644-0132-402S",
        "Desc":"Full Printer"}
    ],

    "DistributionPCB":[
        {"id": 1,
        "Name":"PCB, DISTRIBUTION",
        "PartNum": "210-0360-001S",
        "Desc":"For Series 4 and Series 4e units. For Serial #'s above UG-07470 and UH-01900 Control Panel PCB - Distribution PCB cabling has MTA type connectors. One end has 14 pin connector, opposite end has 11 and 4 pin connectors."},

        {"id": 2,
        "Name":"PCB, DISTRIBUTION",
        "PartNum": "210-0260-001S",
        "Desc":"For Series 4 and Series 4e units. For Serial #'s below UG-07470 and UH-01900 Control Panel PCB - Distribution PCB cable connection is a flat ribbon cable (SCSI type)"}
    ],

    "Addons":[
        {"id": 1,
        "Desc":"Tube Vend With Drop Vault Base"},

        {"id": 2,
        "Desc":"Storage Vault with Drop Vault Base"},

        {"id": 3,
        "Desc":"Tube Vend with Storage Vault and Drop Vault Base"},

        {"id": 4,
        "Desc":"Tube Vend with Mailbox Vault Base"},

        {"id": 5,
        "Desc":"Storage Vault with Mailbox Vault Base"},

        {"id": 6,
        "Desc":"Storage Vault with Tube Vend and Mailbox Vault Base"},

        {"id": 7,
        "Desc":"Small Drop Vault base and additional Narrow Storage vault"},

        {"id": "A",
        "Desc":"Small Drop Vault base and additional (old style) wider Storage vault "},

        {"id": "B",
        "Desc":"Mailbox Vault base and additional (old style) wider Storage vault"},

        {"id": "C",
        "Desc":"Small Drop Vault base and additional (old style) wider Storage vault and Tube Vend Module"},

        {"id": "D",
        "Desc":"Mailbox Vault base and additional (old style) wider Storage vault and Tube Vend Module"}
    ],

    "Power":[
        {"id": 1,
        "Name":"POWER SUPPLY",
        "PartNum": "642-0015-101S",
        "Desc":"For Series 4 units only. Left Side +24 VDC"},

        {"id": 2,
        "Name":"POWER SUPPLY",
        "PartNum": "642-0002-101S",
        "Desc":"For Series 4 units only. Right Side +5 VDC and +12 VDC"}
    ],

    "Display":[
        {"id": 1,
        "Name":"DISPLAY/TOUCHSCREEN ASSEMBLY WITH BACKLIGHT BULB",
        "PartNum": "633-0020-007S"}
    ],



    function parsePartNum (partNum) {
        this.partNum = partNum;
        console.log(partNum);
    }



$('#subForm').click(function() {

        var partNumIn = $('#partNum').val().replace(/-/g, "").trim();
        var serialNumIn = $('#serialNum').val().replace(/-/g, "").trim();
        console.log(partNumIn + " " + serialNumIn);
        $("#currentPart").html("Part Number: " + partNumIn);
        $("#currentSerial").html("Part Number: " + serialNumIn);
        getSafeParts();
        getSafeType();
        function getSafeParts () {
            switch(partNumIn.substr(2,1)) {
                case "1":
                console.log(s4Parts.Cabinet[0].Desc);
                break;
            }

        }

        function getSafeType () {

            switch(serialNumIn.substr(0,2).toLowerCase()) {
                case "ug":
                console.log("Series 4");
                break;

                case "uh":
                this.type= "Series 4";
                break;

                case "fb":
                this.type= "Series 4E";
                break;

                case "ut":
                this.type= "Titan";
                break;

                case "ua":
                this.type= "SCD";
                break;

                case "ub":
                this.type= "SCD";
                break;

                case "uc":
                this.type= "SCD";
                break;

                case "ud":
               this.type= "SCM";
                break;

                case "ue":
                this.type= "SCM";
                break;

                case "ct":
                this.type= "Series 3";
                break;
            }
        }

})

});
