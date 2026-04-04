sudo pacman -S git cmake base-devel
git clone https://github.com/ggerganov/llama.cpp
mkdir models
cd llama.cpp
make
