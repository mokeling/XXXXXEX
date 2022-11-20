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

跳过支持版本验证