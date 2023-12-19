// script.js
const socket = io();
// const socket = io("http://192.168.13.123:5000");
socket.on('connect',function(){
    console.log("connected with socket ID : ${socket.id}");
});
// var uploadspeed = 0
// var downloadspeed =0
// socket.on('server_message', function (data) {
//     console.log('Received data from Flask:', data.data);
//     document.querySelector("#altitude1").innerHTML = "" + data.data;
// });

//socket for altitude
// socket.on('parameters', function(data) {
//     console.log('Received altitude update:', data.data);
//     document.querySelector("#altitude1_dis").innerHTML="Altitude : "+data.data+" m";
// });
$(document).ready(function() {
    var altimeter1 = $.flightIndicator('#altimeter1', 'altimeter');
    altimeter1.setAltitude(0);
    socket.on('parameters', function(data) {
        console.log('Received altitude update:', data.data);
        const altitudeInFeet = data.data * 3.28084;
        altimeter1.setAltitude(altitudeInFeet);
        document.querySelector("#altitude1_dis").innerHTML="Altitude : "+data.data+" m";
    });
    
})


// socket for yaw
// socket.on('yaw_data',function(data){
//     document.querySelector("#yaw_display").innerHTML=" YAW : "+data.data;
// })

$(document).ready(function() {
    var heading1 = $.flightIndicator('#heading1', 'heading');
    heading1.setHeading(0);
    socket.on('yaw1_dis', function(data) {
        heading1.setHeading(data.data);
        document.querySelector("#heading1_dis").innerHTML="YAW : "+data.data;
    });
    
})



function connect() {
    fetch('/drone_connect', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message)
        //document.querySelector("#connection").innerHTML=data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function takeOff(event) {
    event.preventDefault();
    const altitude = document.getElementById('altitude').value;
    console.log(altitude);
    fetch('/takeoff', {
        method: 'POST',
        body: JSON.stringify({ altitude: altitude }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function land() {
    fetch('/land', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function RTL() {
    fetch('/RTL', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function yaw(event) {
    event.preventDefault();
    const yaw = document.getElementById('yaw').value;
    console.log(yaw);
    fetch('/yaw', {
        method: 'POST',
        body: JSON.stringify({ yaw: yaw }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function speedtest() {
    fetch('/networkspeed', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        
        const downloadspeed = Math.floor(data.download_speed);
        document.querySelector("#Downloadspeed").innerHTML="Download Speed : "+downloadspeed;
        console.log(downloadspeed);
        const uploadspeed = Math.floor(data.upload_speed);
        document.querySelector("#Uploadspeed").innerHTML="Upload Speed : "+uploadspeed;
        console.log(uploadspeed);


        $(document).ready(function() {
            $("#demo1").gauge(uploadspeed, {
                min: 0,
                max: 100,
                unit: " Mpbs",
                color: "red",
                colorAlpha: 1,
                bgcolor: "#222",
                type: "default"
            });
        
            $("#demo2").gauge(downloadspeed, {
                min: 0,
                max: 100,
                unit: " Mpbs",
                color: "green",
                colorAlpha: 1,
                bgcolor: "#222",
                type: "default"
            });
        });

    })
    .catch(error => {
        console.error('Error:', error);
    });
}




const socketc = io("http://192.168.13.42:5001");
socketc.on('connect',function(){
    console.log("connected with socket ID : ${socketc.id}");
});

$(document).ready(function() {
    var altimeter2 = $.flightIndicator('#altimeter2', 'altimeter');
    altimeter2.setAltitude(0);
    socketc.on('parameters', function(data) {
        console.log('Received altitude update:', data.data);
        const altitudeInFeet = data.data * 3.28084;
        altimeter2.setAltitude(altitudeInFeet);
        document.querySelector("#altitude2_dis").innerHTML="Altitude : "+data.data+" m";
    });
    
})


$(document).ready(function() {
    var heading2 = $.flightIndicator('#heading2', 'heading');
    heading2.setHeading(0);
    socketc.on('yaw1_dis', function(data) {
        heading2.setHeading(data.data);
        document.querySelector("#heading2_dis").innerHTML="YAW : "+data.data;
    });
    
})

$(document).ready(function() {
    $("#demo1").gauge(0, {
        min: 0,
        max: 100,
        unit: " Mpbs",
        color: "red",
        colorAlpha: 1,
        bgcolor: "#222",
        type: "default"
    });

    $("#demo2").gauge(0, {
        min: 0,
        max: 100,
        unit: " Mpbs",
        color: "green",
        colorAlpha: 1,
        bgcolor: "#222",
        type: "default"
    });
});
// // JavaScript code for drone control

// // Simulated drone object
// const drone = {
//     altitude: 0,
//     takeOff: function() {
//         // Logic for drone takeoff
//         this.altitude = 10; // Set initial altitude to 10 meters
//         updateAltitudeDisplay();
//     },
//     land: function() {
//         // Logic for drone landing
//         this.altitude = 0; // Set altitude to 0 meters
//         updateAltitudeDisplay();
//     }
// };

// // Function to update altitude display
// function updateAltitudeDisplay() {
//     const altitudeDisplay = document.getElementById('altitudeDisplay');
//     altitudeDisplay.textContent = `Altitude: ${drone.altitude} meters`;
// }

// // Event listeners for buttons
// const takeoffBtn = document.getElementById('takeoffBtn');
// const landBtn = document.getElementById('landBtn');

// takeoffBtn.addEventListener('click', () => {
//     drone.takeOff();
// });

// landBtn.addEventListener('click', () => {
//     drone.land();
// });
