// JavaScript code for drone control

// Simulated drone object
const drone = {
    altitude: 0,
    takeOff: function() {
        // Logic for drone takeoff
        this.altitude = 10; // Set initial altitude to 10 meters
        updateAltitudeDisplay();
    },
    land: function() {
        // Logic for drone landing
        this.altitude = 0; // Set altitude to 0 meters
        updateAltitudeDisplay();
    }
};

// Function to update altitude display
function updateAltitudeDisplay() {
    const altitudeDisplay = document.getElementById('altitudeDisplay');
    altitudeDisplay.textContent = `Altitude: ${drone.altitude} meters`;
}

// Event listeners for buttons
const takeoffBtn = document.getElementById('takeoffBtn');
const landBtn = document.getElementById('landBtn');

takeoffBtn.addEventListener('click', () => {
    drone.takeOff();
});

landBtn.addEventListener('click', () => {
    drone.land();
});
