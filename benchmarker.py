import pygame
from OpenGL.GL import *
import numpy as np
import matplotlib.pyplot as plt
import psutil
import time
from dataclasses import dataclass

@dataclass
class GPUBenchmarkResult:
    fps: float
    frame_time_ms: float
    memory_usage_mb: float
    gpu_name: str

class GPUBenchmark:
    def __init__(self, width=1920, height=1080):
        pygame.init()
        pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
        self.width = width
        self.height = height
        
    def run_test(self, duration=10):
        frames = 0
        start_time = time.time()
        frame_times = []
        
        while time.time() - start_time < duration:
            test_start = time.time()
            
            # Render test scene
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self._render_test_scene()
            pygame.display.flip()
            
            frame_time = (time.time() - test_start) * 1000
            frame_times.append(frame_time)
            frames += 1
            
        avg_fps = frames / duration
        avg_frame_time = np.mean(frame_times)
        memory_usage = psutil.Process().memory_info().rss / 1024 / 1024
        
        return GPUBenchmarkResult(
            fps=avg_fps,
            frame_time_ms=avg_frame_time,
            memory_usage_mb=memory_usage,
            gpu_name=self._get_gpu_name()
        )

    def _render_test_scene(self):
        # Complex rendering test
        glBegin(GL_TRIANGLES)
        for _ in range(10000):
            glVertex3f(np.random.random(), np.random.random(), 0)
        glEnd()

    def _get_gpu_name(self):
        # Basic GPU detection
        renderer = glGetString(GL_RENDERER).decode()
        return renderer

class BenchmarkVisualizer:
    def __init__(self):
        self.reference_gpus = {
            "RTX 3080": {"fps": 240, "frame_time": 4.2, "memory": 2048},
            "RTX 2070": {"fps": 144, "frame_time": 6.9, "memory": 1024},
            "GTX 1660": {"fps": 90, "frame_time": 11.1, "memory": 512}
        }

    def create_comparison_graphs(self, result: GPUBenchmarkResult):
        metrics = ["fps", "frame_time", "memory"]
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        for idx, metric in enumerate(metrics):
            gpu_names = list(self.reference_gpus.keys()) + [result.gpu_name]
            values = [self.reference_gpus[gpu][metric] for gpu in self.reference_gpus]
            
            if metric == "fps":
                values.append(result.fps)
            elif metric == "frame_time":
                values.append(result.frame_time_ms)
            else:
                values.append(result.memory_usage_mb)
                
            axes[idx].bar(gpu_names, values)
            axes[idx].set_title(f"{metric.upper()} Comparison")
            axes[idx].tick_params(axis='x', rotation=45)
            
        plt.tight_layout()
        plt.savefig("benchmark_results.png")

def main():
    benchmark = GPUBenchmark()
    print("Running benchmark...")
    result = benchmark.run_test()
    print(f"\nResults for {result.gpu_name}:")
    print(f"FPS: {result.fps:.1f}")
    print(f"Frame Time: {result.frame_time_ms:.1f}ms")
    print(f"Memory Usage: {result.memory_usage_mb:.0f}MB")
    
    visualizer = BenchmarkVisualizer()
    visualizer.create_comparison_graphs(result)
    print("\nBenchmark graphs saved as 'benchmark_results.png'")

if __name__ == "__main__":
    main()