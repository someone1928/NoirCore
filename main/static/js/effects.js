document.addEventListener("DOMContentLoaded", () => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    camera.position.z = 5;
  
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("bg-canvas"), alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
  
    const geometry = new THREE.TorusKnotGeometry(1, 0.3, 128, 16);
    const material = new THREE.MeshStandardMaterial({ color: 0x8a2be2, wireframe: false });
    const torus = new THREE.Mesh(geometry, material);
    scene.add(torus);
  
    const pointLight = new THREE.PointLight(0xffffff);
    pointLight.position.set(5, 5, 5);
    scene.add(pointLight);
  
    function animate() {
      requestAnimationFrame(animate);
      torus.rotation.x += 0.01;
      torus.rotation.y += 0.01;
      renderer.render(scene, camera);
    }
  
    animate();
  });
  