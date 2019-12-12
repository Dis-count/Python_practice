#!/bin/bash

### set user variable <<<
### 备份目录	###
backDir="/mnt/disk/backup/raspberry/"
### 备份文件名	###
firstName="origin"
### 后缀名		###
endName=".tar.gz"
### 增量名		###
secName="_incremental_"
### 非备份位置	###
notBack=" -–exclude=/proc -–exclude=/lost+found -–exclude=/mnt -–exclude=/sys --exclude=/tmp"
### user variable over >>>

function createOrigin()
{
	rm ${firstName}${secName}*${endName}
	rm snapshot
	echo -e "开始创建初始基准备份文件 \t"$firstName$endName
	time tar -g snapshot -zcpvf `echo ${firstName}${endName}` / --exclude=/proc --exclude=/lost+found --exclude=/mnt --exclude=/sys --exclude=/tmp
	echo $?
	echo -e "初始基准备份文件创建完毕 \t"$firstName$endName
}

function createInc()
{
	echo "开始创建增量备份文件"
	for i in {1..100};
	do
		incName=${firstName}${secName}"${i}"${endName};
		if [ -f ${incName} ];
		then 		
			echo "${incName} 已存在"
			continue
		else
			echo "创建增量备份文件 ${incName}"
			time tar -g snapshot -zcpvf `echo ${incName}` /  --exclude=/proc --exclude=/lost+found --exclude=/mnt --exclude=/sys --exclude=/tmp
			echo $?
			echo -e "增量备份文件创建完毕\t"${incName}
			break
		fi
	done
}

if [ -d ${backDir} ];
then
	echo -e ${backDir}"\t备份目录已创建"
else
	mkdir -pv ${backDir}
fi

cd ${backDir}

if [ -f ${firstName}${endName} ];
then
	echo -e ${firstName}${endName}"\t初始基准备份文件已创建"
	ls -al ${firstName}${endName}
	createInc
else
	createOrigin
fi

