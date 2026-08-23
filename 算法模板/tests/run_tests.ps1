param(
    [string]$Compiler = ""
)

$ErrorActionPreference = "Stop"
$testRoot = $PSScriptRoot
$projectRoot = Split-Path -Parent $testRoot
$templateDirectory = Get-ChildItem -LiteralPath $projectRoot -Directory -Recurse `
    -Filter "XCPC_Templates" | Select-Object -First 1
if ($null -eq $templateDirectory) {
    throw "Template include directory not found."
}
$includeRoot = $templateDirectory.FullName

if ([string]::IsNullOrWhiteSpace($Compiler)) {
    $gpp = Get-Command g++ -ErrorAction SilentlyContinue
    if ($null -ne $gpp) {
        $Compiler = $gpp.Source
    } elseif (Test-Path -LiteralPath "D:\app_edge\w64devkit\bin\g++.exe") {
        $Compiler = "D:\app_edge\w64devkit\bin\g++.exe"
    } else {
        throw "g++ was not found. Pass its path with -Compiler."
    }
}

$hasNonAsciiPath = $projectRoot -match "[^\x00-\x7F]"
if ($hasNonAsciiPath) {
    $buildRoot = [System.IO.Path]::GetTempPath()
    $executable = Join-Path $buildRoot "xcpc-template-tests-$PID.exe"
} else {
    $buildRoot = Join-Path $testRoot ".build"
    New-Item -ItemType Directory -Path $buildRoot -Force | Out-Null
    $executable = Join-Path $buildRoot "template_tests.exe"
}
$sources = @(
    (Join-Path $testRoot "test_templates.cpp"),
    (Join-Path $testRoot "odr_probe.cpp")
)
$arguments = @(
    "-std=c++17",
    "-Wall",
    "-Wextra",
    "-Werror",
    "-O2",
    "-I$includeRoot"
) + $sources + @("-o", $executable)

Write-Host "Checking standalone headers..."
$probe = Join-Path $testRoot "header_probe.cpp"
$headers = Get-ChildItem -LiteralPath $includeRoot -Recurse -Filter "*.hpp"
foreach ($header in $headers) {
    $relativeHeader = $header.FullName.Substring($includeRoot.Length + 1).Replace("\", "/")
    & $Compiler -std=c++17 -Wall -Wextra -Werror "-I$includeRoot" `
        -fsyntax-only -include $relativeHeader $probe
    if ($LASTEXITCODE -ne 0) {
        throw "Standalone header check failed: $relativeHeader"
    }
}
Write-Host "Checked $($headers.Count) standalone headers."

try {
    Write-Host "Compiling template tests..."
    & $Compiler @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Compilation failed with exit code $LASTEXITCODE."
    }

    Write-Host "Running template tests..."
    & $executable
    if ($LASTEXITCODE -ne 0) {
        throw "Tests failed with exit code $LASTEXITCODE."
    }
} finally {
    if ($hasNonAsciiPath -and (Test-Path -LiteralPath $executable)) {
        Remove-Item -LiteralPath $executable -Force -ErrorAction SilentlyContinue
    }
}
