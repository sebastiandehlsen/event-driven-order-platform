$folders = @(
    "app",
    "app\domain",
    "app\domain\orders",

    "docs",

    "tests",
    "tests\unit",
    "tests\unit\domain"
)

$files = @(
    "app\domain\orders\__init__.py",
    "app\domain\orders\entities.py",
    "app\domain\orders\enums.py",
    "app\domain\orders\events.py",
    "app\domain\orders\exceptions.py",
    "app\domain\orders\value_objects.py",

    "docs\domain-model.md",

    "tests\unit\domain\__init__.py",

    "pyproject.toml",
    ".gitignore"
)

Write-Host "`nCreating folder structure..." -ForegroundColor Cyan

foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "DIR  $folder" -ForegroundColor Green
    }
}

Write-Host "`nCreating files..." -ForegroundColor Cyan

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "FILE $file" -ForegroundColor Yellow
    }
}

Write-Host "`nBootstrap complete." -ForegroundColor Magenta