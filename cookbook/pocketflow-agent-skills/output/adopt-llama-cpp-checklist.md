# Llama.cpp vs. Ollama Setup & Benchmark Checklist

---

## Pre-Setup

1. Confirm your GPU type (NVIDIA, AMD, Intel Arc, or CPU-only).
2. Note your GPU's VRAM capacity to determine which model sizes are viable.
3. Verify Ollama is already installed and working (baseline for comparison).

> **Dependency:** Steps 2–7 depend on knowing your GPU backend from Step 1.

---

## Step 1: Choose Your GPU Backend

4. Match your GPU to the correct backend:
   - NVIDIA RTX 20-series+ → **CUDA**
   - AMD RX 5000+ → **Vulkan**
   - Intel Arc → **Vulkan** (or SYCL via source build)
   - No dedicated GPU → **CPU (AVX2)**
5. Note the corresponding binary filename pattern for your backend.

---

## Step 2: Install Llama.cpp

6. Open the llama.cpp GitHub Releases page.
7. Identify the latest release by date (not version number alone).
8. Download the ZIP matching your backend (e.g., `llama-b4399-bin-win-cuda-cu12.8-x64.zip` for NVIDIA CUDA).
9. Extract the ZIP to `C:\llama.cpp`.
10. Confirm these executables are present in the `bin` folder:
    - `llama-cli.exe`
    - `llama-server.exe`
    - `llama-bench.exe`
    - `llama-quantize.exe`

> **Blocker (advanced only):** If using CUDA graphs or Flash Attention optimizations, build from source instead (requires Git, CMake, and Visual Studio with C++ workload).

---

## Step 3: Download a GGUF Test Model

11. Open a terminal and navigate to `C:\llama.cpp\bin`.
12. Download a test model:
    ```powershell
    .\llama-cli.exe -hf bartowski/Llama-3.2-3B-Instruct-GGUF:Q4_K_M
    ```
13. Confirm the model file (~2 GB) is saved locally.
14. Verify the model fits in your GPU's VRAM:
    - 8 GB VRAM → use 7B–8B models at Q4_K_M
    - 12 GB+ VRAM → can test 13B models

> **Dependency:** Steps 14 onward require the model to be fully resident in VRAM for valid GPU benchmarks.

---

## Step 4: Benchmark Llama.cpp

15. Run the basic benchmark (512-token prompt, 128-token generation, 3 repetitions):
    ```powershell
    .\llama-bench.exe -m .\models\Llama-3.2-3B-Instruct-Q4_K_M.gguf -ngl 99 -p 512 -n 128 -r 3
    ```
16. Record the **pp** (prompt processing) tokens/sec and **tg** (text generation) tokens/sec.
17. Run scenario benchmarks and record results for each:
    - Short prompt / short generation: `-p 128 -n 64`
    - Long prompt / medium generation: `-p 4096 -n 256`
    - Long-context stress test: `-p 8192 -n 128 -r 2`
18. *(NVIDIA only)* Re-run the long-prompt test with Flash Attention enabled (`-fa`) and record any improvement.
19. *(Optional)* Start `llama-server.exe` and do a subjective interactive test:
    ```powershell
    .\llama-server.exe -m .\models\Llama-3.2-3B-Instruct-Q4_K_M.gguf -ngl 99 -c 4096 --host 0.0.0.0 --port 8080
    ```

---

## Step 5: Benchmark Ollama for Comparison

20. Pull the equivalent model in Ollama:
    ```powershell
    ollama pull llama3.2:3b
    ```
21. Run Ollama with verbose output:
    ```powershell
    ollama run llama3.2:3b --verbose
    ```
22. Use a prompt of known approximate token length and record:
    - `prompt eval rate` (tokens/sec)
    - `eval rate` (tokens/sec)
    - `total duration`
23. *(Optional)* Run the community benchmark script for averaged, repeatable results.

---

## Step 6: Make the Comparison Fair

24. Ensure both tools use the same context window size (e.g., `-c 4096`).
25. Match thread count (`-t`) and batch size (`-b 512`) in llama.cpp to Ollama's defaults where possible.
26. If llama.cpp prompt eval speed looks unexpectedly low, experiment with `-ub` (micro-batch size) and `-b` flags to tune buffer allocation.
27. Re-run any tests that produced anomalous results before drawing conclusions.

> **Blocker:** Results are invalid for comparison if the model is not fully GPU-offloaded in both tools.

---

## Step 7: (Optional) Run Llama-Server as a Persistent Service

28. Launch `llama-server` with your preferred production settings:
    ```powershell
    .\llama-server.exe -m .\models\Llama-3.2-3B-Instruct-Q4_K_M.gguf -ngl 99 -c 8192 --host 0.0.0.0 --port 8080 --api-key your-secret-key
    ```
29. Confirm the OpenAI-compatible endpoint is reachable at `http://localhost:8080/v1/chat/completions`.
30. Point your existing OpenAI-compatible client at the new base URL to verify it works.

---

## Troubleshooting Checklist

31. **"CUDA error: out of memory"** → Reduce `-ngl` or switch to a smaller quantization (e.g., IQ3_XS).
32. **iGPU conflict detected** → Run `.\llama-cli.exe --list-devices`, then specify `--device CUDA0` (or the correct device).
33. **Unexpectedly slow inference** → Add llama.cpp folder and model directory to your antivirus exclusion list.

---

## Definition of Done

- [ ] Llama.cpp is installed with the correct GPU backend binary.
- [ ] A GGUF model is downloaded and confirmed to fit in VRAM.
- [ ] `llama-bench` has been run for at least three prompt/generation scenarios; results are recorded.
- [ ] Ollama has been benchmarked with the same model under the same scenarios; results are recorded.
- [ ] Both sets of numbers are compared side-by-side (pp t/s, tg t/s, TTFT).
- [ ] Any anomalous results have been investigated and retested.
- [ ] A decision has been made: continue with llama.cpp, stay on Ollama, or run both on separate ports.