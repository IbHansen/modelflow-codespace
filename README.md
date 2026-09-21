# ModelFlow Codespace

Open this repository in GitHub Codespaces and you get a Linux machine with
Miniforge and a conda environment `modelflow` containing ModelFlow from the
`ibh` channel plus JupyterLab.

## Start

On GitHub: **Code → Codespaces → Create codespace on main**.

The first build takes several minutes (the environment is solved and
downloaded). At the end the creation log runs `.devcontainer/smoke_test.py`,
which prints the Python version, where `modelclass` was imported from, and
whether Graphviz is available.

## Use

- **Jupyter Notebook starts automatically** each time VS Code connects to the
  codespace (open it with **Open in browser**). It runs in its own terminal and
  opens `notebooks/start.ipynb` in a new browser tab without asking for a
  token (the file list is at `/tree`, or **File → Open**). If the tab does not
  appear (pop-up blocked), open the **Ports** tab and click the globe icon on
  port 8888. Keep the port **private**: with no token, anyone with the link
  could run code if it were public.
- **Notebooks in VS Code:** open or create an `.ipynb` file and pick the kernel
  `modelflow` (`/opt/conda/envs/modelflow/bin/python`).
- **JupyterLab:** in a terminal run `jupyter lab --no-browser`; Codespaces
  forwards port 8888 and offers to open it in the browser.
- **JupyterLab as the editor:** set *Editor preference → JupyterLab* at
  <https://github.com/settings/codespaces>, or on <https://github.com/codespaces>
  use **⋯ → Open in → JupyterLab** for an existing codespace.
- **Terminal:** new terminals start with `modelflow` activated.
  `conda install -c conda-forge <pkg>` works without sudo.

## Files

| File | Purpose |
|---|---|
| `notebooks/start.ipynb` | Start notebook, opened when the codespace starts |
| `environment.yml` | The conda environment: change packages or the Python version here |
| `.devcontainer/Dockerfile` | Ubuntu + Miniforge, builds the environment |
| `.devcontainer/devcontainer.json` | Codespaces/VS Code setup: extensions, ports, smoke test |
| `.devcontainer/smoke_test.py` | Import check run after the codespace is created |

After changing `environment.yml` or anything in `.devcontainer/`, run
**Codespaces: Rebuild Container** from the command palette.
