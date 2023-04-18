local _border = "rounded"
require('lspconfig.ui.windows').default_options = {
  border = _border
}
local lsp = vim.lsp
lsp.handlers["textDocument/hover"] = lsp.with(vim.lsp.handlers.hover, {
  border = _border
})
lsp.handlers['textDocument/signatureHelp'] = vim.lsp.with(
  vim.lsp.handlers.signature_help,
  { border = _border }
)
-- vim.lsp.handlers["textDocument/publishDiagnostics"] = vim.lsp.with(
--   vim.lsp.diagnostic.on_publish_diagnostics, {
--     underline    = false,
--     virtual_text = false,
--     float        = { border = "rounded" },
--   }
-- )

vim.diagnostic.config({
  float = {
    border = _border,
  },
})
