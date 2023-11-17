CFLAGS   := -Wall -Wextra -g -O0
CXXFLAGS := -std=c++20

SRC_DIR   := ./src
SRC_FILE  := main.cpp
BUILD_DIR := ./build
BIN_DIR   := ./bin
EXEC      := main

%: $(SRC_DIR)/%/$(SRC_FILE)
	mkdir -p $(BUILD_DIR)/$(BIN_DIR)/$@/
	$(CXX) $(CXXFLAGS) $(CFLAGS) -o $(BUILD_DIR)/$(BIN_DIR)/$@/$(EXEC) $(SRC_DIR)/$@/$(SRC_FILE)

.PHONY: clean
clean:
	rm -r $(BUILD_DIR)
