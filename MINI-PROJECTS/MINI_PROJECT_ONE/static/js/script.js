import * as THREE from 'three';
import { PointerLockControls } from 'three/addons/controls/PointerLockControls.js';
// import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { Sky } from 'three/addons/objects/Sky.js';

 let mouse = {x:0, y:0}

// --- Core Setup ---
const scene = new THREE.Scene();

// Skybox setup
const sky = new Sky();
sky.scale.setScalar( 450000 );
scene.add(sky);
const skyUniforms = sky.material.uniforms;
skyUniforms[ 'turbidity' ].value = 1; // Increased for hazier, less saturated sky
skyUniforms[ 'rayleigh' ].value = 1; // Reduced for less blue, more muted
skyUniforms[ 'mieCoefficient' ].value = 0.5; // Low for subtle clouds
skyUniforms[ 'mieDirectionalG' ].value = 1;
const sun = new THREE.Vector3();
const phi = THREE.MathUtils.degToRad( 20 ); // Sun position for light
const theta = THREE.MathUtils.degToRad( 180 );
sun.setFromSphericalCoords( 1, phi, theta );
skyUniforms[ 'sunPosition' ].value.copy( sun );

// Ground
const groundGeometry = new THREE.PlaneGeometry( 1000, 1000 );
const groundMaterial = new THREE.MeshBasicMaterial( { color: "rgb(0, 79, 33)" } );
const ground = new THREE.Mesh( groundGeometry, groundMaterial );
scene.add( ground );
ground.rotateX(-1.57)

// Houses
const houseGeometry = new THREE.BoxGeometry( 100, 100, 100 );
const houseMaterial = new THREE.MeshBasicMaterial( { color: 0x00ff00 } ); // here we can add { map: the picture uploaded } 
const cube = new THREE.Mesh( houseGeometry, houseMaterial );
const cube1 = new THREE.Mesh( houseGeometry, houseMaterial );
const cube2 = new THREE.Mesh( houseGeometry, houseMaterial );
scene.add( cube, cube1, cube2 );
console.log(houseGeometry)
cube.position.y = ground.position.y + 50
cube1.position.y = ground.position.y + 50
cube2.position.y = ground.position.y + 50
cube1.position.x = 150
cube2.position.x = 350


// const axesHelper = new THREE.AxesHelper(1)
// scene.add(axesHelper)


const raycaster = new THREE.Raycaster()


const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 2000);
camera.position.set(0, 20, 300);
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
document.body.appendChild(renderer.domElement);

const controls = new PointerLockControls( camera, renderer.domElement );
// const controls = new OrbitControls(camera, renderer.domElement)

// FPS movement variables
let moveForward = false;
let moveBackward = false;
let moveLeft = false;
let moveRight = false;
let moveUp = false; // Flag for upward movement
let moveDown = false; // Flag for downward movement
const speed = 500; // Controls speed of movement
const velocity = new THREE.Vector3(); // For smooth movement

// Key event handlers for FPS movement
function onKeyDown(event) { // Sets movement flags on key press
    switch (event.code) {
        case 'ArrowUp':
        case 'KeyW':
            moveForward = true;
            break;
        case 'ArrowLeft':
        case 'KeyA':
            moveLeft = true;
            break;
        case 'ArrowDown':
        case 'KeyS':
            moveBackward = true;
            break;
        case 'ArrowRight':
        case 'KeyD':
            moveRight = true;
            break;
        case 'Space': // Spacebar for upward movement
            moveUp = true;
            break;
        case 'KeyC': // C key for downward movement
            moveDown = true;
            break;
    }
}

function onKeyUp(event) { // Resets movement flags on key release
    switch (event.code) {
        case 'ArrowUp':
        case 'KeyW':
            moveForward = false;
            break;
        case 'ArrowLeft':
        case 'KeyA':
            moveLeft = false;
            break;
        case 'ArrowDown':
        case 'KeyS':
            moveBackward = false;
            break;
        case 'ArrowRight':
        case 'KeyD':
            moveRight = false;
            break;
        case 'Space': // Reset upward movement
            moveUp = false;
            break;
        case 'KeyC': // Reset downward movement
            moveDown = false;
            break;
    }
}

document.addEventListener('keydown', onKeyDown);
document.addEventListener('keyup', onKeyUp);
document.addEventListener('click', () => controls.lock()); // Locks mouse pointer for FPS look

// --- Lighting ---
const ambientLight = new THREE.AmbientLight(0xffffff, 0.3); // Soft overall illumination
scene.add(ambientLight);

const light = new THREE.DirectionalLight( 0xFFFFFF, 0.5 ); // Main directional light source
scene.add(light);

let elapsedTime = 0;
function animate(timer) { // Main animation loop
    requestAnimationFrame(animate);
    
    const delta = 0.001*(timer - elapsedTime) ; // Time since last frame
    elapsedTime = timer;
   

    // FPS movement in camera direction
    const moveVector = new THREE.Vector3(); // Accumulates desired movement direction
    if (moveForward) {
        const forward = new THREE.Vector3();
        camera.getWorldDirection(forward); // Get camera's forward vector
        moveVector.add(forward);
    }
    if (moveBackward) {
        const backward = new THREE.Vector3();
        camera.getWorldDirection(backward);
        moveVector.add(backward.negate()); // Opposite of forward
    }
    if (moveLeft) {
        const left = new THREE.Vector3();
        camera.getWorldDirection(left).cross(camera.up); // Calculate left vector
        moveVector.add(left.negate());
    }
    if (moveRight) {
        const right = new THREE.Vector3();
        camera.getWorldDirection(right).cross(camera.up); // Calculate right vector
        moveVector.add(right);
    }
    if (moveUp) {
        moveVector.add(camera.up); // Move upward along camera's up vector
    }
    if (moveDown) {
        moveVector.add(camera.up.clone().negate()); // Move downward
    }
    if (moveVector.length() > 0) {
        moveVector.normalize().multiplyScalar(speed); // Normalize and scale by speed
    }
    
    // Smooth movement with velocity interpolation
    velocity.lerp(moveVector, 0.1); // Gradually approach target velocity
    camera.position.add(velocity.clone().multiplyScalar(delta)); // Apply movement

    // Collision detection with terrain - smooth adjustment
    const targetY = ground.position.y + 20; // Desired minimum height above terrain
    if (camera.position.y < targetY) {
        camera.position.y = THREE.MathUtils.lerp(camera.position.y, targetY, 0.1); // Smoothly adjust height
    }
    
    // Prevent camera from going beyond terrain bounds
    camera.position.x = THREE.MathUtils.clamp(camera.position.x, -1000, 1000); // Clamp X position
    camera.position.z = THREE.MathUtils.clamp(camera.position.z, -1000, 1000); // Clamp Z position

    raycaster.setFromCamera(mouse, camera);
    
    renderer.render(scene, camera);
    const objectsToTest = [cube, cube1, cube2]
    const intersects = raycaster.intersectObjects(objectsToTest)

     for(const object of objectsToTest)
    {
        object.material.color.set('#ff0000')
    }

    for(const intersect of intersects)
    {
        intersect.object.material.color.set('#0000ff')
    }
}


animate(0);

// Handle window resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight; // Update camera aspect ratio
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight); // Resize renderer
});

// Handle click on start
document.getElementById('start-btn').addEventListener('click', function () {
                const overlay = document.getElementById('intro-overlay');
                overlay.classList.add('hidden');
                setTimeout(() => overlay.remove(), 700);
            })

window.addEventListener("mousemove", function(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1; //map to between -1,1
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1; //map to between -1,1
//   console.log(mouse);
})

window.onload = function () {
    console.log("js is up and running");
    document
        .querySelector("#insertImageForm")
        .addEventListener("submit", async function (event) {
            event.preventDefault();
            console.log("cat submitted")

            let form = document.querySelector("#insertImageForm")
            let data = new FormData(form)
            try {
                let res = await fetch("/thank_form_two", {
                    method: "POST",
                    body: data,
                });
                let resJSON = await res.json();
                console.log(resJSON);
                document.querySelector("#result-container").innerHTML =
                    `<p>Thanks for submitting your cat!</p>
           <img src="/static/uploads/${resJSON.filename}">`;

            } catch (err) {
                console.log(err);
            }
        })


};
