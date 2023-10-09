# XIVLauncherEX

天地万象を我が意のままに！

XLCN Version:6.3.2.0

## PATCH

工具：[dnSpyEx/dnSpy](https://github.com/dnSpyEx/dnSpy)

#### XIVLauncher.Common.Dalamud

##### AssetManager.CheckAssetRefreshNeeded

IL:26 ldstr

```
"https://raw.githubusercontent.com/gamous/XIVLauncherEX/main/Asset/meta"
```

取消插件黑名单

只是为了Unban的话后面的都不用看了

**请勿分发Patch过的文件 否则停止更新**

##### DalamudLauncher.ReCheckVersion

IL:10  brfalse.s

```
brtrue.s
```

**跳过支持版本验证**

##### DalamudLauncher.CanRunDalamud

无视支持版本强制启动


##### DalamudUpdater.UpdateDalamud

IL:74
```
br.s 76(00ED)	ldloc.3
```

无视Key验证进入测试通道

#### Dalamud.Support

##### EventTracking.SendMeasurement

停止发送统计

IL:130 ldstr

```
ldstr "https://127.0.0.1"
```

##### EventTracking.CheatBannedLength

不修改

#### Dalamud.Game

##### ChatHandlers.OnChatMessage

IL:40 ldloc.0

```
br 57 ldarg.1
```
另一种停止发送统计

#### Dalamud.Plugin.Internal

##### PluginManager.IsManifestBanned

另一种取消插件黑名单

###### PluginManager.PluginManager

`bannedplugin.json`和`cheatplugin.json`长度检查

## CONFIG

#### dalamudConfig.json

"DalamudBetaKey": **[Version["Key"]](https://github.com/ottercorp/dalamud-distrib/blob/main/stg/version)**

Dalamud测试通道KEY



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

> https://aonyx.ffxiv.wang/Dalamud/Asset/Meta
