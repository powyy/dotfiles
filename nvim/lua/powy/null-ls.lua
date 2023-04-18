local null_ls = require 'null-ls'

local formatting = null_ls.builtins.formatting
local diagnostics = null_ls.builtins.diagnostics
null_ls.setup {
  sources = {
    formatting.prettier.with({ extra_args = { '--tab-width=4', '--use-tab' } }),
    formatting.gofumpt,
    formatting.goimports,
    -- diagnostics.eslint_d,
    diagnostics.flake8,
    -- null_ls.builtins.completion.spell,
  },
}
