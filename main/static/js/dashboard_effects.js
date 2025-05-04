document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("dash-bg");
    if (!canvas) return;
  
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
    camera.position.z = 5;
  
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true });
    renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  
    const geometry = new THREE.SphereGeometry(1.5, 32, 32);
    const material = new THREE.MeshStandardMaterial({ color: 0x6c5ce7, wireframe: true });
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);
  
    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(5, 5, 5);
    scene.add(light);
  
    function animate() {
      requestAnimationFrame(animate);
      sphere.rotation.x += 0.005;
      sphere.rotation.y += 0.01;
      renderer.render(scene, camera);
    }
  
    animate();
  });
  