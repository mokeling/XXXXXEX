# XIVLauncherEX

天地万象を我が意のままに！

## PATCH

工具：[dnSpyEx/dnSpy](https://github.com/dnSpyEx/dnSpy)

#### XIVLauncher.Common.Dalamud

##### AssetManager.CheckAssetRefreshNeeded

IL:19 ldstr

```
"https://raw.githubusercontent.com/gamous/XIVLauncherEX/main/Asset/meta"
```

取消插件黑名单

##### DalamudLauncher.ReCheckVersion

IL:10  brfalse.s

```
brtrue.s
```

**跳过支持版本验证**



## CONFIG

#### dalamudConfig.json

"DalamudBetaKey": **[Version["Key"]](https://github.com/ottercorp/dalamud-distrib/blob/main/stg/version)**

Dalamud测试通道



## ENVIRONMENT

#### XIVLauncher.Common.EnvironmentSettings

XL启动器本体设置

| SettingsVariable          | EnvironmentVariable       | Description          |
| ------------------------- | ------------------------- | -------------------- |
| IsWine                    | XL_WINEONLINUX            |                      |
| IsHardwareRendered        | XL_HWRENDER               |                      |
| IsDisableUpdates          | XL_NOAUTOUPDATE           | 关闭XL启动项更新检查 |
| IsPreRelease              | XL_PRERELEASE             | 开启XL启动器测试版本 |
| IsNoRunas                 | XL_NO_RUNAS               |                      |
| IsIgnoreSpaceRequirements | XL_NO_SPACE_REQUIREMENTS" |                      |



### 