-- Anything related to editor theme
require('catppuccin').setup {
    flavour = 'mocha', -- latte, frappe, macchiato, mocha
    background = {
        -- :h background
        light = 'latte',
        dark = 'mocha',
    },
    transparent_background = false,
    show_end_of_buffer = false, -- show the '~' characters after the end of buffers
    term_colors = true,
    dim_inactive = {
        enabled = false,
        shade = 'dark',
        percentage = 0.15,
    },
    no_italic = false, -- force no italic
    no_bold = false,   -- force no bold
    styles = {
        comments = { 'italic' },
        conditionals = { 'italic' },
        loops = {},
        functions = {},
        keywords = {},
        strings = {},
        variables = {},
        numbers = {},
        booleans = {},
        properties = {},
        types = {},
        operators = {},
    },
    color_overrides = {},
    custom_highlights = {},
    integrations = {
        cmp = true,
        gitsigns = true,
        nvimtree = true,
        telescope = true,
        notify = true,
        mini = false,
        harpoon = true,
        mason = true,
        -- native_lsp = true,
        treesitter = true,
        -- lsp_trouble = true,
        -- for more plugins integrations please scroll down (https://github.com/catppuccin/nvim#integrations)
    },
}
vim.cmd.colorscheme 'catppuccin-mocha'
-- vim.api.nvim_set_hl(0, 'normal', { bg = 'none' })
-- vim.api.nvim_set_hl(0, 'normalfloat', { bg = 'none' })

-- set line number color
-- vim.api.set
vim.api.nvim_set_hl(0, 'LineNr', { fg = '#cba6f7', bold = true })
-- vim.api.nvim_set_hl(0, 'cusorlinenr', { fg = '#cba6f7', bold = true })
-- :hi linenr guibg=#000000 guifg=#ffffff

require("mason").setup({
    ui = {
        border = "rounded"
    }
})
