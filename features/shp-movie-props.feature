Feature: Movie shape properties
  In order to interact with movie shapes
  As a developer using python-pptx
  I need a set of properties describing a movie shape


  Scenario: Movie shape
    Given a movie shape
     Then movie is a Movie object


  @wip
  Scenario: Movie.shape_type
    Given a movie shape
     Then movie.shape_type is MSO_SHAPE_TYPE.MEDIA


  @wip
  Scenario: Movie.media_type
    Given a movie shape
     Then movie.media_type is PP_MEDIA_TYPE.MOVIE


  @wip
  Scenario: Movie.media_format
    Given a movie shape
     Then movie.media_format is a _MediaFormat object