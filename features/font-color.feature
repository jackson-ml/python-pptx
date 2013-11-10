Feature: Query and set font color
  In order to color text to suit a presentation application
  As a developer using python-pptx
  I need to query and set the color of text

  @wip
  Scenario Outline: Get font color type
     Given a font with <color type> color
      Then the font's color type is <value>

  Examples: Color type settings
    | color type | value       |
    | no         | None        |
    | an RGB     | RGB         |
    | a theme    | theme color |

  @wip
  Scenario: Get font RGB color
    Given a font with an RGB color
     Then its color value matches its RGB color

  @wip
  Scenario: Get font theme color
    Given a font with a theme color
     Then its color value matches its theme color

  @wip
  Scenario Outline: Get font color brightness
    Given a font with a color brightness setting of <setting>
     Then its color brightness value is <value>

  Examples: Color brightness settings
    | setting                  | value |
    | 25% darker               | -0.25 |
    | 40% lighter              |  0.4  |
    | no brightness adjustment |  0    |

  @wip
  Scenario Outline: Set font color
    Given a font with no color
     When I set the font <color type> value
      And I save and reload the presentation
     Then the font's <color type> value matches the value I set

  Examples: Color types
    | color type  |
    | RGB         |
    | theme color |

  @wip
  Scenario Outline: Set font color brightness
    Given a font with <color type> color
     When I set the font color brightness value
      And I save and reload the presentation
     Then the font's color brightness matches the value I set

  Examples: Color types
    | color type |
    | an RGB     |
    | a theme    |