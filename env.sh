#!/bin/bash
TOPDIR=`pwd`
export PATH=$TOPDIR/cmake-3.14.5-Linux-x86_64/bin:$PATH

# fix libisl.so.19 not found issue
export LD_LIBRARY_PATH=$TOPDIR/kendryte-toolchain/bin:$LD_LIBRARY_PATH

generate_envsh() {
	cat <<-EOT
	CONFIG_TOOLCHAIN_PATH="${TOPDIR}/kendryte-toolchain/bin"
	CONFIG_TOOLCHAIN_PREFIX="riscv64-unknown-elf-"
	EOT
}

generate_envsh > .config.mk
