;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!

(setq user-full-name "Cezar Cruz"
      user-mail-address "cezarcruz@outlook.com")

;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets. It is optional.
;; Doom exposes five (optional) variables for controlling fonts in Doom:
;;
;; - `doom-font' -- the primary font to use
;; - `doom-variable-pitch-font' -- a non-monospace font (where applicable)
;; - `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;; - `doom-unicode-font' -- for unicode glyphs
;; - `doom-serif-font' -- for the `fixed-pitch-serif' face
;;
;; See 'C-h v doom-font' for documentation and more examples of what they
;; accept. For example:
;;
;;(setq doom-font (font-spec :family "Fira Code" :size 12 :weight 'semi-light)
;;      doom-variable-pitch-font (font-spec :family "Fira Sans" :size 13))
;;
;; If you or Emacs can't find your font, use 'M-x describe-font' to look them
;; up, `M-x eval-region' to execute elisp code, and 'M-x doom/reload-font' to
;; refresh your font settings. If Emacs still can't find your font, it likely
;; wasn't installed correctly. Font issues are rarely Doom issues!

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-one)

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")


;; Whenever you reconfigure a package, make sure to wrap your config in an
;; `after!' block, otherwise Doom's defaults may override your settings. E.g.
;;
;;   (after! PACKAGE
;;     (setq x y))
;;
;; The exceptions to this rule:
;;
;;   - Setting file/directory variables (like `org-directory')
;;   - Setting variables which explicitly tell you to set them before their
;;     package is loaded (see 'C-h v VARIABLE' to look up their documentation).
;;   - Setting doom variables (which start with 'doom-' or '+').
;;
;; Here are some additional functions/macros that will help you configure Doom.
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;; Alternatively, use `C-h o' to look up a symbol (functions, variables, faces,
;; etc).
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.


(setq-default tab-width 2)
(setq doom-font "JetBrains Mono:pixelsize=20")

(setq mac-command-modifier 'meta)
(setq mac-option-modifier 'super)
(setq confirm-kill-emacs nil
      read-process-output-max (* 1024 1024)
      compilation-scroll-output nil)

(add-to-list 'default-frame-alist '(fullscreen . maximized))


(use-package! cider
  :after clojure-mode
  :config
  (setq cider-show-error-buffer t
        cider-font-lock-dynamically nil
        cider-eldoc-display-for-symbol-at-point nil
        cider-prompt-for-symbol nil
        cider-use-xref nil
        cider-test-defining-forms '("deftest" "defspec" "defflow"))

  (set-lookup-handlers! '(cider-mode cider-repl-mode) nil)
  (set-popup-rule! "'cider-test-report*" :side 'right :width 0.4)
  (set-popup-rule! "^\\*cider-repl" :side 'bottom :quit nil)
  (add-hook 'cider-mode-hook (lambda () (remove-hook 'completion-at-point-functions #'cider-complete-at-point))))

(use-package! clojure-mode
  :config (setq clojure-ident-style 'align-arguments))

(use-package! lsp-ui
  :after lsp-mode
  :commands lsp-ui-mode
  :config
  (setq lsp-ui-doc-enable nil
        lsp-ui-peek-enable nil))

(use-package! paredit
  :hook ((clojure-mode . paredit-mode)
         (emacs-lisp-mode . paredit-mode)))

(setq face-remapping-alist
'((show-paren-match . (:inherit pulsar-yellow)) ;; yellow highlight
  (show-paren-mismatch . (:inherit flycheck-error)))) ;; red squiggly underline


(use-package! pulsar
  :init
  (setq pulsar-pulse t
        pulsar-delay 0.05
        pulsar-iterations 5
        pulsar-face 'pulsar-yellow
        pulsar-highlight-face 'pulsar-magenta)
  (pulsar-global-mode t)
  :config
  ;; integration with the `consult' package:
  (add-hook 'consult-after-jump-hook #'pulsar-recenter-top)
  (add-hook 'consult-after-jump-hook #'pulsar-reveal-entry)

  ;; integration with the built-in `isearch':
  (add-hook 'isearch-mode-end-hook #'pulsar-recenter-middle)
  (advice-add 'isearch-forward :after #'pulsar-recenter-middle)
  (advice-add 'isearch-repeat-forward :after #'pulsar-recenter-middle)
  (advice-add 'isearch-backward :after #'pulsar-recenter-middle)
  (advice-add 'isearch-repeat-backward :after #'pulsar-recenter-middle)

  ;; integration with the built-in `imenu':
  (add-hook 'imenu-after-jump-hook #'pulsar-recenter-top)
  (add-hook 'imenu-after-jump-hook #'pulsar-reveal-entry))


(when (modulep! :completion vertico)
  (use-package! vertico
    :demand t
    :bind
    (("M-."      . #'embark-act)
     ("C-x B"    . #'+vertico/switch-workspace-buffer)
     :map vertico-map
     ("C-l"      . #'vertico-directory-up)) ;; behave like helm to go up a level
    :config
    (setq vertico-cycle t
          read-extended-command-predicate #'command-completion-default-include-p
          orderless-matching-styles     '(orderless-literal
                                          orderless-initialism
                                          orderless-regexp)
          completion-category-defaults  '((email (styles substring)))
          completion-category-overrides '((file (styles +vertico-basic-remote
                                                        orderless
                                                        partial-completion)))

          marginalia-align              'right))

  (use-package! consult
    :config
    (setq consult-grep-args
          "grep --null --line-buffered --color=never --ignore-case \
--exclude-dir=.git --line-number -I -r .")
    :bind
    (("M-i"     . #'consult-imenu)
     ("C-c M-o" . #'consult-multi-occur)
     ("C-x b"   . #'consult-buffer)
     ("C-x 4 b" . #'consult-buffer-other-window)
     ("C-x 5 b" . #'consult-buffer-other-frame)
     ("C-x r b" . #'consult-bookmark)
     ("M-g g"   . #'consult-goto-line))))

(when (modulep! :completion company)
  (use-package! company
    :defer t
    :config
    (setq company-idle-delay 0.9)))

(use-package! clojure-mode
  :defer t
  :hook (clojure-mode . rainbow-delimiters-mode)
  :config
  (when (modulep! :tools lsp)
    (map! :map clojure-mode-map
          "C-c j d"    #'lsp-ui-doc-glance
          "C-c j i"    #'lsp-ui-imenu)
    (add-hook! '(clojure-mode-local-vars-hook
                 clojurec-mode-local-vars-hook
                 clojurescript-mode-local-vars-hook)
      (defun +clojure-disable-lsp-indentation-h ()
        (setq-local lsp-enable-indentation nil))
      #'lsp!)
    (after! lsp-clojure
      (dolist (m '(clojure-mode
                   clojurec-mode
                   clojurescript-mode
                   clojurex-mode))
        (add-to-list 'lsp-language-id-configuration (cons m "clojure")))
      (dolist (dir '("[/\\\\]\\.clj-kondo\\'"
                     "[/\\\\]\\.cp-cache\\'"
                     "[/\\\\]\\.lsp\\'"
                     "[/\\\\]\\.shadow-cljs\\'"
                     "[/\\\\]\\target\\'"))
        (add-to-list 'lsp-file-watch-ignored dir)))
    (setq lsp-lens-enable          t       ;; enable LSP code lens for inline reference counts
          lsp-file-watch-threshold 2000
          lsp-enable-snippet       t)))
