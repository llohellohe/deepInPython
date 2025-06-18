
https://github.com/kortix-ai/suna/blob/main/docs/SELF-HOSTING.md

# 安装过程中的失败
## brew
brew install 失败，提示奇怪的错误
解决方案：
* which brew 查看是否是 /opt/homebrew/bin/brew
* 重新安装home brew


其它一些重新安装
```
alias docker="/opt/homebrew/bin/podman"
alias brew="/opt/homebrew/bin/brew"

source /Users/yangqi/.nvm/nvm.sh
alias node="/Users/yangqi/.nvm/versions/node/v22.16.0/bin/node"
alias npm="/Users/yangqi/.nvm/versions/node/v22.16.0/bin/npm"
```

## supabase
需要配置data api
![[Pasted image 20250606212745.png]]

# 一些配置文件
# Docker


报错后，需要重新安装homebrew，确保路径为/opt/homebrew/bin/brew

### podman
podman machine list
podman machine rm XXX https://github.com/containers/podman/issues/15742
podman machine init
podman machine start



```
➜  ~ podman machine init
Looking up Podman Machine image at quay.io/podman/machine-os:5.5 to create VM
Getting image source signatures
Copying blob 3f2d2b32431f done   |
Copying config 44136fa355 done   |
Writing manifest to image destination
3f2d2b32431fe1ab9071babe5816f487bf2a26b5bf0df18aeb6151689da02b6a
Extracting compressed file: podman-machine-default-arm64.raw: done
Machine init complete
To start your machine run:

	podman machine start

➜  ~    podman machine start
Starting machine "podman-machine-default"


This machine is currently configured in rootless mode. If your containers
require root permissions (e.g. ports < 1024), or if you run into compatibility
issues with non-podman clients, you can switch using the following command:

	podman machine set --rootful

API forwarding listening on: /var/folders/cr/wd1dfkbd3_b289qf907nh89r0000gp/T/podman/podman-machine-default-api.sock

The system helper service is not installed; the default Docker API socket
address can't be used by podman. If you would like to install it, run the following commands:

        sudo /opt/homebrew/Cellar/podman/5.5.0/bin/podman-mac-helper install
        podman machine stop; podman machine start

You can still connect Docker API clients by setting DOCKER_HOST using the
following command in your terminal session:

        export DOCKER_HOST='unix:///var/folders/cr/wd1dfkbd3_b289qf907nh89r0000gp/T/podman/podman-machine-default-api.sock'

Machine "podman-machine-default" started successfully
```

设置内存
podman machine init -m XXX 设置内存大小


## 加载配置文件
```
def load_env_data():  
    if os.path.exists(ENV_DATA_FILE):  
        with open(ENV_DATA_FILE, 'r') as f:  
            return json.load(f)  
    return {  
        'supabase': {},  
        'daytona': {},  
        'llm': {},  
        'search': {},  
        'rapidapi': {}  
    }
```


