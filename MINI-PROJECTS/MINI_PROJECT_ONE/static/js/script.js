import * as THREE from 'three';
import { PointerLockControls } from 'three/addons/controls/PointerLockControls.js';
import { Sky } from 'three/addons/objects/Sky.js';
// import { TextGeometry } from 'three/addons/geometries/TextGeometry.js'; // not working
// import { FontLoader } from 'three/addons/loaders/FontLoader.js';

let mouse = { x: 0, y: 0 }
let lastPoint = null;

// --- Core Setup ---
const scene = new THREE.Scene();

// texture loader:
const textureLoader = new THREE.TextureLoader();


// Skybox setup
const sky = new Sky();
sky.scale.setScalar(450000);
scene.add(sky);
const skyUniforms = sky.material.uniforms;
skyUniforms['turbidity'].value = 1; // Increased for hazier, less saturated sky
skyUniforms['rayleigh'].value = 1; // Reduced for less blue, more muted
skyUniforms['mieCoefficient'].value = 0.5; // Low for subtle clouds
skyUniforms['mieDirectionalG'].value = 1;
const sun = new THREE.Vector3();
const phi = THREE.MathUtils.degToRad(20); // Sun position for light
const theta = THREE.MathUtils.degToRad(180);
sun.setFromSphericalCoords(1, phi, theta);
skyUniforms['sunPosition'].value.copy(sun);

// --- Lighting ---
const ambientLight = new THREE.AmbientLight(0xffffff, 0.3); // Soft overall illumination
scene.add(ambientLight);

const light = new THREE.DirectionalLight(0xFFFFFF, 5); // Main directional light source
light.position.set(-150, 100, -100);
light.target.position.set(-300, 0, 0);
scene.add(light);
scene.add(light.target);

light.castShadow = true
light.shadow.mapSize.width = 1024
light.shadow.mapSize.height = 1024
light.shadow.radius = 10

// const helper = new THREE.DirectionalLightHelper(light);
// scene.add(helper);

// Ground
const groundGeometry = new THREE.PlaneGeometry(10000, 10000);
const groundMaterial = new THREE.MeshBasicMaterial({ color: "rgb(0, 79, 33)" });
const ground = new THREE.Mesh(groundGeometry, groundMaterial);
scene.add(ground);
ground.rotateX(- Math.PI * 0.5)

// Houses
const box = {
    width: 100,
    height: 100,
    depth: 10,
}
const block_texture = `/static/assets/block_description.png`;
textureLoader.load(block_texture, (texture) => {
    const cube = new THREE.Mesh(
        new THREE.BoxGeometry(box.width, box.height, box.depth),
        new THREE.MeshBasicMaterial({ map: texture })
    );
    const cubePosition = ground.position.y + 50
    scene.add(cube);
    cube.position.y = cubePosition
    cube.position.x = -150

    cube.receiveShadow = true
    cube.castShadow = true
})
const cube = new THREE.Mesh(
    new THREE.BoxGeometry(box.width, box.height, box.depth),
    new THREE.MeshBasicMaterial({ color: "rgb(0, 0, 255)" })
);
const cubePosition = ground.position.y + 50
scene.add(cube);
cube.position.y = cubePosition
cube.position.x = -150


// // activate to see axes
// const axesHelper = new THREE.AxesHelper(100)
// scene.add(axesHelper)
ground.receiveShadow = true

const raycaster = new THREE.Raycaster()


const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 2000);
camera.position.set(0, 20, 300);
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;
document.body.appendChild(renderer.domElement);

const controls = new PointerLockControls(camera, renderer.domElement);
// const controls = new OrbitControls(camera, renderer.domElement)

// FPS movement variables
let moveForward = false;
let moveBackward = false;
let moveLeft = false;
let moveRight = false;
let moveUp = false; // Flag for upward movement
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
            setTimeout(() => moveUp = false, 100) // to avoid player breaking out of bounds!
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
    }
}

document.addEventListener('keydown', onKeyDown);
document.addEventListener('keyup', onKeyUp);
// Locks mouse pointer for FPS look

// dot to replace cursor
const dot = new THREE.Mesh(
    new THREE.SphereGeometry(0.04, 16, 16),
    new THREE.MeshBasicMaterial({
        color: "black",
        name: 'material-1',
        opacity: 0.4,
        transparent: true,
    })
);
dot.position.set(0, 0, -2); // 2 units ahead of the camera
camera.add(dot);
scene.add(camera);


let elapsedTime = 0;
function animate(timer) { // Main animation loop
    requestAnimationFrame(animate);

    const delta = 0.001 * (timer - elapsedTime); // Time since last frame
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
    else if (camera.position.y < targetY + 30) { // Collision with invisible aerian boundary
        camera.position.y = THREE.MathUtils.lerp(camera.position.y, targetY, 0.1); // Smoothly adjust height
    }

    // Prevent camera from going beyond terrain bounds
    camera.position.x = THREE.MathUtils.clamp(camera.position.x, -800, 800); // Clamp X position
    camera.position.z = THREE.MathUtils.clamp(camera.position.z, -800, 800); // Clamp Z position

    raycaster.setFromCamera(new THREE.Vector2(0, 0), camera);

    renderer.render(scene, camera);
    const objectsToTest = [cube]
    const intersects = raycaster.intersectObjects(objectsToTest)

    // the 3d point on the cube!
    // console.log(intersects[0].point)
    if (intersects.length > 0) { // basically if intersects is true
        lastPoint = intersects[0].point
        console.log("intersecting box")
        window.addEventListener('click', makeFormAppear);
    } else {
        lastPoint = null;
        window.removeEventListener('click', makeFormAppear);
        window.addEventListener('click', makeFormDisappear)
    }


    for (const object of objectsToTest) {
        object.material.color.set('#0000ff')
    }

    for (const intersect of intersects) {
        intersect.object.material.color.set('#ff0000')
    }
}

animate(0);

function makeFormAppear() {
    const overlayForm = document.getElementById('insertImageForm');
    overlayForm.classList.add('showing');
    // exits pointer lock controls so user can click
    controls.unlock()
}

function makeFormDisappear() {
    const overlayForm = document.getElementById('insertImageForm');
    overlayForm.classList.remove('showing');
}

function placeCatInWorld(filename) {
    const url = `/static/uploads/${filename}`;

    textureLoader.load(url, (texture) => {
        const catPlane = new THREE.Mesh(
            new THREE.BoxGeometry(20, 20, 11),
            new THREE.MeshBasicMaterial({ map: texture })
        );
        catPlane.position.set(lastPoint.x, lastPoint.y, lastPoint.z - 5);
        scene.add(catPlane);
    });
}

function placeOtherCats(filename, i) {
    const url = `/static/uploads/${filename}`;

    textureLoader.load(url, (texture) => {
        const cat = new THREE.Mesh(
            new THREE.BoxGeometry(50, 50, 50),
            new THREE.MeshBasicMaterial({ map: texture })
        );

        if (i <= 5) {
            cat.position.set(i * 75, 25, 100);
        }
        else if (i <= 10) {
            cat.position.set(i * 75 - 450, 25, 200);
        }
        else if (i <= 15) {
            cat.position.set(i * 75 - 450, 25, 0);
        }
        scene.add(cat);
    });
}

async function displayPastCats() {
    try {
        let res = await fetch("/pastUploads");
        let files = await res.json()
        console.log(files)
        files.forEach((filename, i) => {
            placeOtherCats(filename, i)
        });

    } catch (err) {
        console.log(err)
    }
}

// Handle window resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight; // Update camera aspect ratio
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight); // Resize renderer
});

// Handle click on start
document.getElementById('start-btn').addEventListener('click', () => {
    const overlay = document.getElementById('intro-overlay');
    overlay.classList.add('hidden');
    setTimeout(() => overlay.remove(), 700);
    controls.lock();
})

window.addEventListener("mousemove", function (event) {
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1; //map to between -1,1
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1; //map to between -1,1
    //   console.log(mouse);
})


window.onload = function () {
    console.log("js is up and running");
    displayPastCats();


    document.querySelector("#insertImageForm").addEventListener("submit", async function (event) {
        event.preventDefault();
        console.log("cat submitted")

        makeFormDisappear();
        controls.lock();

        let form = document.querySelector("#insertImageForm")
        let data = new FormData(form)


        try {
            let res = await fetch("/catForm", {
                method: "POST",
                body: data,
            });
            let resJSON = await res.json();
            console.log(resJSON);
            document.querySelector("#result-container").innerHTML =
                ` Thanks for submitting your cat!`;
            placeCatInWorld(resJSON.filename)

        } catch (err) {
            console.log(err);
        }

        displayPastCats();
    })


};
